<?php
/**
 * EcoCare Cleaning Services Limited — PHP Form Processor (Native Clenix Fallback)
 * Handles inquiries sent via Clenix's native jQuery AJAX handler.
 */

header('Content-Type: application/json; charset=UTF-8');

if ($_SERVER['REQUEST_METHOD'] !== 'POST') {
    http_response_code(405);
    echo json_encode(['success' => false, 'message' => 'Method Not Allowed']);
    exit;
}

// 1. Honeypot Spam Check
if (!empty($_POST['website_url']) || !empty($_POST['_gotcha']) || !empty($_POST['hp_field'])) {
    echo json_encode(['success' => true, 'message' => 'Thank you for contacting EcoCare!']);
    exit;
}

// 2. Sanitize Inputs
$name = isset($_POST['name']) ? trim(strip_tags($_POST['name'])) : '';
$phone = isset($_POST['phone']) ? trim(strip_tags($_POST['phone'])) : '';
$email = isset($_POST['email']) ? trim(filter_var($_POST['email'], FILTER_SANITIZE_EMAIL)) : '';
$subject = isset($_POST['subject']) ? trim(strip_tags($_POST['subject'])) : 'General Inquiry';
$message = isset($_POST['message']) ? trim(strip_tags($_POST['message'])) : '';

// 3. Validation
$errors = [];
if (strlen($name) < 2) {
    $errors[] = 'Full name is required (minimum 2 characters).';
}
if (empty($phone) && empty($email)) {
    $errors[] = 'Please provide either a phone number or email address.';
}
if (!empty($phone) && strlen(preg_replace('/[^0-9]/', '', $phone)) < 9) {
    $errors[] = 'Please enter a valid telephone number.';
}
if (!empty($email) && !filter_var($email, FILTER_VALIDATE_EMAIL)) {
    $errors[] = 'Please enter a valid email address.';
}
if (strlen($message) < 5) {
    $errors[] = 'Please enter a message (minimum 5 characters).';
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

// 4. Save to Submissions Storage
$submission = [
    'type' => 'contact_php',
    'name' => $name,
    'phone' => $phone,
    'email' => $email,
    'subject' => $subject,
    'message' => $message,
    'ip' => $_SERVER['REMOTE_ADDR'] ?? 'unknown',
    'receivedAt' => date('c')
];

$storageDir = __DIR__ . '/../../data';
if (!is_dir($storageDir)) {
    @mkdir($storageDir, 0755, true);
}
@file_put_contents($storageDir . '/submissions.jsonl', json_encode($submission) . "\n", FILE_APPEND | LOCK_EX);

// 5. Send via PHP mail() if available
$to = 'ecocaregh1on1@gmail.com';
$emailSubject = "EcoCare Contact: " . $subject;
$emailBody = "Name: $name\nPhone: $phone\nEmail: $email\nSubject: $subject\n\nMessage:\n$message\n\nReceived: " . date('Y-m-d H:i:s');
$headers = "From: webmaster@ecocaregh.com\r\nReply-To: " . ($email ?: $to) . "\r\nX-Mailer: PHP/" . phpversion();

@mail($to, $emailSubject, $emailBody, $headers);

// 6. Return Success Response for Clenix main.js
echo json_encode([
    'success' => true,
    'message' => 'Message has been sent successfully. Thank you for contacting EcoCare!',
    'data' => [
        'name' => $name,
        'whatsapp' => 'https://wa.me/233249014253'
    ]
]);

