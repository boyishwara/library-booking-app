import os
import time
from datetime import datetime, timedelta
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

BASE_URL = "http://localhost:8000"

def get_driver():
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')
    options.add_argument('--disable-gpu')
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')
    driver = webdriver.Chrome(options=options)
    driver.implicitly_wait(5)
    return driver

def login(driver, email, password):
    driver.get(BASE_URL + "/login")
    WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.NAME, "identifier")))
    driver.find_element(By.NAME, "identifier").send_keys(email)
    driver.find_element(By.NAME, "password").send_keys(password)
    driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()
    time.sleep(1.5)

def logout(driver):
    driver.delete_all_cookies()
    driver.get(BASE_URL + "/login")
    time.sleep(1)

def cleanup_drafts(driver):
    try:
        while True:
            driver.get(BASE_URL + "/my-bookings")
            time.sleep(1)
            lihat_draft_btns = driver.find_elements(By.XPATH, "//a[contains(@href, '/bookings/draft?id=')]")
            if len(lihat_draft_btns) > 0:
                driver.execute_script("arguments[0].click();", lihat_draft_btns[0])
                time.sleep(1)
                delete_btn = driver.find_element(By.XPATH, "//button[contains(translate(., 'ABCDEFGHIJKLMNOPQRSTUVWXYZ', 'abcdefghijklmnopqrstuvwxyz'), 'hapus draft booking')]")
                driver.execute_script("arguments[0].click();", delete_btn)
                time.sleep(1)
                try:
                    driver.switch_to.alert.accept()
                except:
                    pass
                time.sleep(1)
            else:
                break
    except Exception as e:
        pass

def fill_booking_form(driver, tanggal, mulai, selesai, tujuan, room_id=1, upload_file=None):
    driver.get(BASE_URL + f"/rooms/show?id_ruangan={room_id}")
    time.sleep(1.5)
    
    js_remove_validation = """
    ['tanggal_penggunaan_ruang', 'waktu_mulai', 'waktu_selesai', 'tujuan', 'pegawai_reason', 'pegawai_file'].forEach(name => {
        let el = document.getElementsByName(name)[0];
        if (el) {
            el.removeAttribute('required');
            el.removeAttribute('min');
            el.removeAttribute('max');
        }
    });
    """
    driver.execute_script(js_remove_validation)
    
    # Active form inputs are usually the last ones if there's a blur overlay. But wait, `test_full.py` used [0]
    # In `test_full.py`, `[0]` worked because the active form input was indeed [0] if no blur overlay.
    # But wait, if there IS a blur overlay (e.g. TC-INT-04 Library Closure), then [0] might be the blurred one!
    # Let's set ALL matching inputs.
    driver.execute_script(f"document.querySelectorAll('[name=\"tanggal_penggunaan_ruang\"]').forEach(el => el.value = '{tanggal}');")
    driver.execute_script(f"document.querySelectorAll('[name=\"waktu_mulai\"]').forEach(el => el.value = '{mulai}');")
    driver.execute_script(f"document.querySelectorAll('[name=\"waktu_selesai\"]').forEach(el => el.value = '{selesai}');")
    driver.execute_script(f"document.querySelectorAll('[name=\"tujuan\"]').forEach(el => el.value = '{tujuan}');")
    
    if upload_file:
        driver.execute_script(f"document.querySelectorAll('[name=\"pegawai_reason\"]').forEach(el => el.value = 'rapat');")
        try:
            inputs = driver.find_elements(By.NAME, "pegawai_file")
            for inp in inputs:
                try:
                    inp.send_keys(upload_file)
                except:
                    pass
        except:
            pass

    submit_btn = driver.find_element(By.XPATH, "//button[contains(., 'Buat Draft Booking')]")
    driver.execute_script("arguments[0].click();", submit_btn)
    
    try:
        WebDriverWait(driver, 5).until(
            lambda d: len(d.find_elements(By.CSS_SELECTOR, "div.text-red-800 p.font-medium")) > 0 or "/bookings/draft" in d.current_url
        )
    except:
        pass
        
    try:
        err = driver.find_element(By.CSS_SELECTOR, "div.text-red-800 p.font-medium").text
        return err.lower()
    except:
        return ""

def get_next_weekday(dt, add_days=1):
    target = dt
    added = 0
    while added < add_days:
        target += timedelta(days=1)
        if target.weekday() < 5:
            added += 1
    return target

def run_integration_tests():
    print('Running DB Setup...')
    os.system('php setup_db_for_test.php')

    driver = get_driver()
    date_conflict = '2026-06-15'
    date_conflict_user = '2026-06-16'
    date_closure = '2026-06-17'
    
    print("==================================================")
    print("1. STARTING INTEGRATION AUTOMATION TESTING (SELENIUM)")
    print("==================================================")
    
    try:
        logout(driver)
        # TC-INT-01, TC-INT-02 & TC-INT-03
        login(driver, "mahasiswa@stu.pnj.ac.id", "akumahasiswa")
        cleanup_drafts(driver)
        
        # TC-INT-01
        # Test Case: Valid Booking Draft Creation
        # Simulates a user creating a valid booking draft without conflicts on a regular weekday.
        today = datetime.now()
        date_valid = get_next_weekday(today, 4).strftime('%Y-%m-%d')
        err = fill_booking_form(driver, date_valid, "09:00", "11:00", "Diskusi Kelompok", room_id=1)
        passed = err == "" and "draft" in driver.current_url
        if passed:
            try:
                succ = driver.find_element(By.CSS_SELECTOR, "div.text-emerald-800 p.font-medium").text
                passed = "berhasil" in succ.lower() or "draft" in succ.lower()
            except:
                pass
        print(f"[TC-INT-01] Draft Berhasil   : {'PASS' if passed else 'FAIL (Err: ' + err[:100] + ')'}")
        cleanup_drafts(driver)
        
        # TC-INT-02
        # Test Case: Room Booking Conflict
        # Attempts to book a room that already has an approved or pending booking at the requested time.
        err = fill_booking_form(driver, date_conflict, "09:00", "11:00", "Diskusi Kelompok", room_id=1)
        passed = "dibooking" in err or "bentrok" in err or "tersedia" in err
        print(f"[TC-INT-02] Room Conflict    : {'PASS' if passed else 'FAIL (Err: ' + err[:100] + ')'}")
        
        # TC-INT-03
        # Test Case: User Booking Conflict
        # Checks the constraint where a user cannot make a booking if they already have an active/pending booking.
        err = fill_booking_form(driver, date_conflict_user, "13:00", "15:00", "Diskusi Kelompok", room_id=2)
        passed = "sudah memiliki" in err or "pic" in err or "aktif" in err or "1 booking per hari" in err
        print(f"[TC-INT-03] User Conflict    : {'PASS' if passed else 'FAIL (Err: ' + err[:100] + ')'}")
        
        # TC-INT-04
        # Test Case: Library Closure Handling
        # Ensures that users cannot book a room on dates when the library is officially closed.
        err = fill_booking_form(driver, date_closure, "09:00", "11:00", "Diskusi Kelompok", room_id=1)
        passed = "diblokir" in err or "tutup" in err or "tersedia" in err
        print(f"[TC-INT-04] Library Closure  : {'PASS' if passed else 'FAIL (Err: ' + err[:100] + ')'}")
        
        logout(driver)
        
        # TC-INT-05
        # Test Case: File Upload for Specific Roles
        # Verifies that users with specific roles (e.g., dosen) can upload supporting documents when booking.
        with open("dummy_surat.pdf", "w") as f:
            f.write("%PDF-1.4 dummy content")
        file_path = os.path.abspath("dummy_surat.pdf")
            
        login(driver, "dosen_test@pnj.ac.id", "akumahasiswa")
        cleanup_drafts(driver)
        
        err = fill_booking_form(driver, date_conflict, "08:00", "10:00", "Diskusi Kelompok", room_id=2, upload_file=file_path)
        
        passed = err == "" and "draft" in driver.current_url
        if passed:
            try:
                succ = driver.find_element(By.CSS_SELECTOR, "div.text-emerald-800 p.font-medium").text
                passed = "berhasil" in succ.lower() or "draft" in succ.lower()
            except:
                pass
        print(f"[TC-INT-05] File Upload      : {'PASS' if passed else 'FAIL (Err: ' + err[:100] + ')'}")
        logout(driver)
        
    finally:
        driver.quit()
        print('Cleaning up DB...')
        os.system('php cleanup_db.php')
        if os.path.exists("dummy_surat.pdf"):
            os.remove("dummy_surat.pdf")

if __name__ == "__main__":
    run_integration_tests()
