<?php
$pdo = new PDO('mysql:host=localhost;dbname=library_booking_app;charset=utf8mb4', 'root', '');
$stmt = $pdo->query('SELECT id_booking, user_id, tanggal_penggunaan_ruang, status, tujuan, waktu_mulai FROM booking');
print_r($stmt->fetchAll(PDO::FETCH_ASSOC));
