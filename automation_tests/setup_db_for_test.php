<?php
// setup_db_for_test.php

$host = 'localhost';
$db   = 'library_booking_app';
$user = 'root';
$pass = '';
$charset = 'utf8mb4';

$dsn = "mysql:host=$host;dbname=$db;charset=$charset";
$options = [
    PDO::ATTR_ERRMODE            => PDO::ERRMODE_EXCEPTION,
    PDO::ATTR_DEFAULT_FETCH_MODE => PDO::FETCH_ASSOC,
    PDO::ATTR_EMULATE_PREPARES   => false,
];

try {
    $pdo = new PDO($dsn, $user, $pass, $options);
} catch (\PDOException $e) {
    throw new \PDOException($e->getMessage(), (int)$e->getCode());
}

echo "Connected to database.\n";

// 1. Setup Suspended User (TC-F-10)
$stmt = $pdo->prepare("SELECT id_user FROM users WHERE email = 'suspended_mhs@stu.pnj.ac.id'");
$stmt->execute();
$userObj = $stmt->fetch();

$passwordHash = password_hash('akumahasiswa', PASSWORD_DEFAULT);

if (!$userObj) {
    $stmt = $pdo->prepare("INSERT INTO users (nama, nim, email, password, nomor_hp, id_role, status) VALUES (?, ?, ?, ?, ?, ?, ?)");
    $stmt->execute(['Suspended Mahasiswa', '1122334455', 'suspended_mhs@stu.pnj.ac.id', $passwordHash, '0812345678', 3, 'suspended']);
    echo "Suspended user created.\n";
} else {
    $stmt = $pdo->prepare("UPDATE users SET status = 'suspended', password = ? WHERE email = 'suspended_mhs@stu.pnj.ac.id'");
    $stmt->execute([$passwordHash]);
    echo "Suspended user updated.\n";
}

// 2. Insert Conflicting Verified Booking (TC-INT-02 and TC-INT-03)
// Clean up existing test verified bookings to prevent duplication
$pdo->exec("DELETE FROM booking");
$pdo->exec("DELETE FROM blocked_dates");

// Get user ID of 'mahasiswa@stu.pnj.ac.id'
$stmt = $pdo->prepare("SELECT id_user FROM users WHERE email = 'mahasiswa@stu.pnj.ac.id'");
$stmt->execute();
$mhs = $stmt->fetch();

if ($mhs) {
    $id_user = $mhs['id_user'];
    
    // TC-INT-02: Room conflict. Create a verified booking on room 1 for tomorrow 09:00 - 11:00.
    // Use a different user (e.g. ID 1) as PIC so it triggers "Room conflict" instead of "User conflict".
    $tomorrow = '2026-06-15';
    
    $stmt = $pdo->prepare("INSERT INTO booking (ruangan_id, user_id, tanggal_penggunaan_ruang, waktu_mulai, waktu_selesai, tujuan, status) 
        VALUES (1, 1, ?, '09:00:00', '11:00:00', 'Test Conflict', 'verified')");
    $stmt->execute([$tomorrow]);
    echo "Room conflict booking created.\n";

    // TC-INT-03: User conflict. Create a verified booking for 'mahasiswa@stu.pnj.ac.id' on 2026-06-16 13:00 - 15:00 in Room 2
    $day2 = '2026-06-16';
    $stmt = $pdo->prepare("INSERT INTO booking (ruangan_id, user_id, tanggal_penggunaan_ruang, waktu_mulai, waktu_selesai, tujuan, status) 
        VALUES (2, ?, ?, '13:00:00', '15:00:00', 'Diskusi Kelompok', 'verified')");
    $stmt->execute([$id_user, $day2]);
    echo "User conflict booking created.\n";
}

// 3. TC-INT-04: Library Closure (Blocked Dates)
// Let's block "the day after tomorrow"
$dayAfterTomorrow = '2026-06-17';
$pdo->exec("DELETE FROM blocked_dates WHERE alasan = 'Maintenance Test'");
$stmt = $pdo->prepare("INSERT INTO blocked_dates (tanggal_begin, tanggal_end, ruangan_id, alasan, created_by) VALUES (?, ?, NULL, 'Maintenance Test', 1)");
$stmt->execute([$dayAfterTomorrow, $dayAfterTomorrow]);
echo "Library closure date created.\n";

// 4. Setup Dosen User (TC-INT-05)
$stmt = $pdo->prepare("SELECT id_user FROM users WHERE email = 'dosen_test@pnj.ac.id'");
$stmt->execute();
$dosenObj = $stmt->fetch();

if (!$dosenObj) {
    $stmt = $pdo->prepare("INSERT INTO users (nama, nip, email, password, nomor_hp, id_role, status) VALUES (?, ?, ?, ?, ?, ?, ?)");
    $stmt->execute(['Dosen Test', '987654321', 'dosen_test@pnj.ac.id', $passwordHash, '0812345679', 2, 'active']);
    echo "Dosen user created.\n";
} else {
    $stmt = $pdo->prepare("UPDATE users SET status = 'active', password = ? WHERE email = 'dosen_test@pnj.ac.id'");
    $stmt->execute([$passwordHash]);
    echo "Dosen user updated.\n";
}

echo "Database setup completed.\n";
