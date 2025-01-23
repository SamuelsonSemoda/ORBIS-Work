<?php
require 'phpmailer/src/PHPMailer.php';
require 'phpmailer/src/SMTP.php';
require 'phpmailer/src/Exception.php';

use PHPMailer\PHPMailer\PHPMailer;
use PHPMailer\PHPMailer\Exception;

$mail = new PHPMailer(true);

try {
    // Server settings
    $mail->Host = 'mail.yourdomain.com'; // Your domain's SMTP server
    $mail->SMTPAuth = true;
    $mail->Username = 'your-email@yourdomain.com'; // Your email address
    $mail->Password = 'your-email-password'; // Your email password
    $mail->SMTPSecure = PHPMailer::ENCRYPTION_STARTTLS; // or ENCRYPTION_SMTPS
    $mail->Port = 587; // Port 587 for STARTTLS or 465 for SSL


    // Recipients
    $mail->setFrom('your-email@gmail.com', 'Web Form');
    $mail->addAddress('recipient-email@example.com'); // Recipient

    // Content
    $mail->isHTML(true);
    $mail->Subject = 'Form Submission';
    $mail->Body = 'This is a test email from PHPMailer.';

    $mail->send();
    echo 'Email sent successfully.';
} catch (Exception $e) {
    echo "Failed to send email. Error: {$mail->ErrorInfo}";
}
?>