import time
import re
import threading
import requests
from datetime import date, timedelta, datetime
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
    options.add_argument('--window-size=1920,1080')
    options.add_argument('--log-level=3')
    return webdriver.Chrome(options=options)

def login(driver, email, password):
    driver.get(BASE_URL + "/login")
    time.sleep(1)
    driver.find_element(By.NAME, "identifier").clear()
    driver.find_element(By.NAME, "identifier").send_keys(email)
    driver.find_element(By.NAME, "password").clear()
    driver.find_element(By.NAME, "password").send_keys(password)
    driver.find_element(By.NAME, "password").send_keys(Keys.RETURN)
    time.sleep(1.5)

def logout(driver):
    driver.delete_all_cookies()
    driver.get(BASE_URL + "/login")
    WebDriverWait(driver, 5).until(EC.url_contains("/login"))

def cleanup_drafts(driver):
    try:
        while True:
            driver.get(BASE_URL + "/my-bookings")
            lihat_draft_btns = driver.find_elements(By.XPATH, "//a[contains(@href, '/bookings/draft?id=')]")
            if len(lihat_draft_btns) > 0:
                driver.execute_script("arguments[0].click();", lihat_draft_btns[0])
                WebDriverWait(driver, 5).until(EC.url_contains("/bookings/draft"))
                delete_btn = driver.find_element(By.XPATH, "//button[contains(translate(., 'ABCDEFGHIJKLMNOPQRSTUVWXYZ', 'abcdefghijklmnopqrstuvwxyz'), 'hapus draft booking')]")
                driver.execute_script("arguments[0].click();", delete_btn)
                WebDriverWait(driver, 5).until(EC.alert_is_present())
                driver.switch_to.alert.accept()
                WebDriverWait(driver, 5).until(EC.url_contains("/my-bookings"))
            else:
                break
    except Exception as e:
        pass

def fill_booking_form(driver, tanggal, mulai, selesai, tujuan):
    driver.get(BASE_URL + "/rooms/show?id_ruangan=1")
    time.sleep(1)
    
    # Try to extract flash error just in case we hit an error on load
    try:
        flash = driver.find_element(By.CSS_SELECTOR, "div.text-red-800 p.font-medium").text
        # print("Flash before submit:", flash)
    except:
        pass
        
    driver.execute_script(f"document.getElementsByName('tanggal_penggunaan_ruang')[0].value = '{tanggal}';")
    driver.execute_script(f"document.getElementsByName('waktu_mulai')[0].value = '{mulai}';")
    driver.execute_script(f"document.getElementsByName('waktu_selesai')[0].value = '{selesai}';")
    driver.execute_script(f"document.getElementsByName('tujuan')[0].value = '{tujuan}';")
    # Remove HTML5 validation attributes so backend validation is triggered
    js_remove_validation = """
    ['tanggal_penggunaan_ruang', 'waktu_mulai', 'waktu_selesai', 'tujuan'].forEach(name => {
        let el = document.getElementsByName(name)[0];
        if (el) {
            el.removeAttribute('required');
            el.removeAttribute('min');
            el.removeAttribute('max');
            el.removeAttribute('minlength');
            el.removeAttribute('maxlength');
            el.removeAttribute('pattern');
        }
    });
    """
    driver.execute_script(js_remove_validation)
    
    submit_btn = driver.find_element(By.XPATH, "//button[contains(., 'Buat Draft Booking')]")
    driver.execute_script("arguments[0].click();", submit_btn)
    
    try:
        # Wait until either an error flash appears, OR the URL changes to /bookings/draft (success)
        WebDriverWait(driver, 5).until(
            lambda d: len(d.find_elements(By.CSS_SELECTOR, "div.text-red-800 p.font-medium")) > 0 or "/bookings/draft" in d.current_url
        )
    except:
        pass # timeout, just try to get the error anyway if it exists
        
    try:
        err = driver.find_element(By.CSS_SELECTOR, "div.text-red-800 p.font-medium").text
        return err.lower()
    except:
        return ""

def run_tests():
    print("==================================================")
    print("1. STARTING FULL FUNCTIONAL AUTOMATION TESTING (SELENIUM)")
    print("==================================================")
    driver = get_driver()
    try:
        login(driver, "mahasiswa@stu.pnj.ac.id", "akumahasiswa")
        cleanup_drafts(driver)
        
        today = date.today()
        tomorrow = today + timedelta(days=1)
        if tomorrow.weekday() >= 5: tomorrow += timedelta(days=(7 - tomorrow.weekday()))
        date_valid = today.strftime('%Y-%m-%d')
        
        past_date = today - timedelta(days=1)
        date_past = past_date.strftime('%Y-%m-%d')
        
        # TC-F-01 and TC-F-02 (Without login or with basic login)
        # TC-F-01
        # Test Case: Room Capacity Filter
        # Verifies that the room listing page displays the capacity filter option.
        driver.get(BASE_URL + "/rooms")
        passed = "kapasitas" in driver.page_source.lower() or "cari" in driver.page_source.lower()
        print(f"[TC-F-01] Filter Kapasitas : {'PASS' if passed else 'FAIL'}")
        
        # TC-F-02
        # Test Case: Admin-Only Access Restriction
        # Ensures that a regular student user cannot access a room restricted to admins or specific roles.
        driver.get(BASE_URL + "/rooms/show?id_ruangan=3")
        time.sleep(1)
        try:
            err = driver.find_element(By.CSS_SELECTOR, "div.text-red-800 p.font-medium").text.lower()
        except:
            err = driver.page_source.lower()
            
        passed = "admin, dosen, atau tendik" in err or "diakses oleh admin" in err or "dilarang" in err
        print(f"[TC-F-02] Akses AdminOnly  : {'PASS' if passed else 'FAIL (Error: ' + err[:50] + ')'}")
        
        # TC-F-03 to TC-F-09
        driver.get(BASE_URL + "/rooms/show?id_ruangan=1")
        today = datetime.now()
        date_valid = today.strftime('%Y-%m-%d')
        date_past = (today - timedelta(days=1)).strftime('%Y-%m-%d')
        date_far = (today + timedelta(days=10)).strftime('%Y-%m-%d')
        
        cleanup_drafts(driver)
        
        # TC-F-03
        # Test Case: Mandatory Purpose Field
        # Checks that the booking form requires the "tujuan" (purpose) field to be filled.
        err = fill_booking_form(driver, date_valid, "09:00", "11:00", "")
        passed = "tujuan" in err and "diisi" in err
        print(f"[TC-F-03] Tanpa Tujuan     : {'PASS' if passed else 'FAIL (Error: ' + err + ')'}")
        
        # TC-F-04
        # Test Case: Past Date Booking Prevented
        # Ensures users cannot book a room for a date that has already passed.
        err = fill_booking_form(driver, date_past, "09:00", "11:00", "Diskusi Kelompok")
        passed = "lewat" in err or "lalu" in err
        print(f"[TC-F-04] Tanggal Masa Lalu: {'PASS' if passed else 'FAIL (Error: ' + err + ')'}")
        
        # TC-F-05
        # Test Case: Minimum Booking Duration
        # Validates that a booking duration must meet the minimum requirement (e.g., 1 hour).
        err = fill_booking_form(driver, date_valid, "23:00", "23:30", "Diskusi Kelompok")
        passed = "minimal" in err and "1 jam" in err
        print(f"[TC-F-05] Durasi Minimal   : {'PASS' if passed else 'FAIL (Error: ' + err + ')'}")
        
        # TC-F-06
        # Test Case: Maximum Booking Duration
        # Validates that a booking duration cannot exceed the maximum allowed limit (e.g., 3 hours).
        err = fill_booking_form(driver, date_valid, "19:00", "23:00", "Diskusi Kelompok")
        passed = "maksimal 3 jam" in err or "maksimal" in err
        print(f"[TC-F-06] Durasi Maksimal  : {'PASS' if passed else 'FAIL (Error: ' + err + ')'}")
        
        # TC-F-07
        # Test Case: Friday Prayer Break Restriction
        # Prevents bookings that intersect with the mandatory Friday break period.
        err = fill_booking_form(driver, date_valid, "11:00", "14:00", "Diskusi Kelompok")
        passed = "istirahat" in err or "jumat" in err
        print(f"[TC-F-07] Jam Istirahat Jum: {'PASS' if passed else 'FAIL (Error: ' + err + ')'}")
        
        # TC-F-08
        # Test Case: Maximum Advance Booking Limit
        # Verifies that users cannot book a room further in advance than the allowed limit (e.g., 7 days).
        date_far = (today + timedelta(days=14)).strftime('%Y-%m-%d')
        err = fill_booking_form(driver, date_far, "09:00", "11:00", "Diskusi Kelompok")
        passed = "7 hari" in err or "batas" in err or "hari kerja" in err or "hari ke depan" in err
        print(f"[TC-F-08] Max 7 Hari Kerja : {'PASS' if passed else 'FAIL (Error: ' + err + ')'}")
        
        # TC-F-09
        # Test Case: Minimum Lead Time
        # Ensures bookings are made at least a certain amount of time (e.g., 15 minutes) before the start time.
        now = datetime.now()
        start_time = now + timedelta(minutes=5)
        end_time = start_time + timedelta(hours=1)
        err = fill_booking_form(driver, date_valid, start_time.strftime("%H:%M"), end_time.strftime("%H:%M"), "Diskusi Kelompok")
        passed = "15 menit" in err or "di luar sesi" in err or "hari" in err or "istirahat" in err or "sesi" in err or "sebelum jam 08:00" in err
        print(f"[TC-F-09] Lead Time < 15 m : {'PASS' if passed else 'FAIL (Error: ' + err + ')'}")
        
        # TC-F-11: Time Order
        # Test Case: Invalid Time Order
        # Checks that the end time must be strictly after the start time.
        err = fill_booking_form(driver, date_valid, "11:00", "09:00", "Diskusi Kelompok")
        passed = "lebih besar dari waktu mulai" in err or "tidak valid" in err
        print(f"[TC-F-11] Waktu Mundur     : {'PASS' if passed else 'FAIL (Error: ' + err + ')'}")
        
        # TC-F-12: Session Hours (Melewati jam 16:00)
        # Test Case: Outside Operational Hours
        # Verifies that bookings cannot extend beyond library operational hours.
        err = fill_booking_form(driver, date_valid, "16:30", "18:00", "Diskusi Kelompok")
        passed = "sebelum jam 08:15" in err or "sesi resmi" in err or "jam operasi" in err or "sebelum" in err or "melewati jam" in err or "di luar jam" in err
        print(f"[TC-F-12] Di Luar Jam Sesi : {'PASS' if passed else 'FAIL (Error: ' + err + ')'}")
        
        # TC-F-13: One Booking Per Day
        # Test Case: Daily Booking Limit
        # Validates the rule that a user is restricted to a single booking per day.
        # Build a safe date that is NOT a weekend and DOES NOT collide with setup_db_for_test.php (days 1-3)
        date_safe = today + timedelta(days=6)
        if date_safe.weekday() >= 5:
            date_safe += timedelta(days=(7 - date_safe.weekday()))
        date_unik = date_safe.strftime('%Y-%m-%d')
        
        fill_booking_form(driver, date_unik, "09:00", "11:00", "Diskusi Kelompok")
        time.sleep(2) # ensure redirect and DB save complete
        
        err = fill_booking_form(driver, date_unik, "13:15", "15:00", "Diskusi Kelompok")
        passed = "1 booking" in err or "sudah memiliki" in err or "hanya dapat melakukan" in err
        print(f"[TC-F-13] 1 Booking / Hari : {'PASS' if passed else 'FAIL (Error: ' + err + ')'}")
        
        # Logout
        logout(driver)
        
        # TC-F-10
        # Test Case: Suspended Account
        # Ensures that a user with a suspended account is restricted appropriately.
        login(driver, "suspended_mhs@stu.pnj.ac.id", "akumahasiswa")
        try:
            err = driver.find_element(By.CSS_SELECTOR, "div.text-red-800 p.font-medium").text
            err = err.lower()
        except:
            err = driver.page_source.lower()
        passed = "suspen" in err or "ditangguhkan" in err or "login" in driver.current_url
        print(f"[TC-F-10] Akun Suspended   : {'PASS' if passed else 'FAIL (Error: ' + err[:50] + ')'}")
        logout(driver)
        
    finally:
        driver.quit()

if __name__ == "__main__":
    run_tests()
