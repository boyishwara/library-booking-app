<?php
$pdo = new PDO('mysql:host=localhost;dbname=library_booking_app', 'root', '');
echo "Blocked Dates:\n";
$stmt = $pdo->query('SELECT * FROM blocked_dates');
print_r($stmt->fetchAll(PDO::FETCH_ASSOC));

echo "Bookings:\n";
$stmt = $pdo->query('SELECT * FROM booking WHERE status="verified"');
print_r($stmt->fetchAll(PDO::FETCH_ASSOC));
