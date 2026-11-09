<?php
/**
 * EcoCare Cleaning Services Limited — PHP Quote Calculator Processor
 */

header('Content-Type: application/json; charset=UTF-8');

if ($_SERVER['REQUEST_METHOD'] !== 'POST') {
    http_response_code(405);
    echo json_encode(['success' => false, 'message' => 'Method Not Allowed']);
    exit;
}

if (!empty($_POST['website_url']) || !empty($_POST['_gotcha']) || !empty($_POST['hp_field'])) {
    echo json_encode(['success' => true, 'message' => 'Thank you for requesting an estimate!']);
    exit;
}

$name = isset($_POST['name']) ? trim(strip_tags($_POST['name'])) : '';
$phone = isset($_POST['phone']) ? trim(strip_tags($_POST['phone'])) : '';
$email = isset($_POST['email']) ? trim(filter_var($_POST['email'], FILTER_SANITIZE_EMAIL)) : '';
$location = isset($_POST['location']) ? trim(strip_tags($_POST['location'])) : '';
$service = isset($_POST['service']) ? trim(strip_tags($_POST['service'])) : 'General Cleaning';
$notes = isset($_POST['message']) ? trim(strip_tags($_POST['message'])) : (isset($_POST['notes']) ? trim(strip_tags($_POST['notes'])) : '');

$errors = [];
if (strlen($name) < 2) {
    $errors[] = 'Full name is required (minimum 2 characters).';
}
if (empty($phone) || strlen(preg_replace('/[^0-9]/', '', $phone)) < 9) {
    $errors[] = 'A valid telephone number is required.';
}
if (empty($location) || strlen($location) < 2) {
    $errors[] = 'Location / Landmark in Accra is required.';
}
if (strlen($notes) < 5) {
    $errors[] = 'Please provide brief details about your property or requirements.';
}

if (!empty($errors)) {
    http_response_code(400);
    echo json_encode([
        'success' => false,
        'message' => implode(' ', $errors),
        'errors' => $errors
    ]);
    exit;
}

$submission = [
    'type' => 'quote_php',
    'name' => $name,
    'phone' => $phone,
    'email' => $email,
    'service' => $service,
    'location' => $location,
    'notes' => $notes,
    'ip' => $_SERVER['REMOTE_ADDR'] ?? 'unknown',
    'receivedAt' => date('c')
];

$storageDir = __DIR__ . '/../../data';
if (!is_dir($storageDir)) {
    @mkdir($storageDir, 0755, true);
}
@file_put_contents($storageDir . '/submissions.jsonl', json_encode($submission) . "\n", FILE_APPEND | LOCK_EX);

$to = 'ecocaregh1on1@gmail.com';
$emailSubject = "EcoCare Quote Request: " . $service . " (" . $name . ")";
$emailBody = "Name: $name\nPhone: $phone\nEmail: $email\nService: $service\nLocation: $location\n\nNotes:\n$notes\n\nReceived: " . date('Y-m-d H:i:s');
$headers = "From: webmaster@ecocaregh.com\r\nReply-To: " . ($email ?: $to) . "\r\nX-Mailer: PHP/" . phpversion();

@mail($to, $emailSubject, $emailBody, $headers);

echo json_encode([
    'success' => true,
    'message' => 'Your quotation request has been received by our Achimota office. Thank you!',
    'data' => [
        'name' => $name,
        'whatsapp' => 'https://wa.me/233249014253'
    ]
]);

