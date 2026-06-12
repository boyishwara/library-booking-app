<?php
$pdo = new PDO('mysql:host=localhost;dbname=library_booking_app;charset=utf8mb4', 'root', '');
$pdo->exec("DELETE FROM booking WHERE user_id IN (SELECT id_user FROM users WHERE email IN ('mahasiswa@stu.pnj.ac.id', 'dosen_test@pnj.ac.id'))");
$pdo->exec("DELETE FROM booking WHERE tujuan = 'Test Conflict'");
$pdo->exec("DELETE FROM blocked_dates WHERE alasan = 'Maintenance Test'");
echo "All test database data cleaned up successfully.\n";
