<?php
if ($_SERVER["REQUEST_METHOD"] == "POST") {
    // Retrieve form data
    $name = $_POST["name"];
    $email = $_POST["email"];
    $subject = $_POST["subject"];
    $message = $_POST["message"];

    // Recipient email address (where the contact form data will be sent)
    $to = "lnu8@uwindsor.ca"; // Replace with your actual email address

    // Email subject
    $email_subject = "New Contact Form Submission: $subject";

    // Email content
    $email_message = "You have received a new contact form submission from $name:\n\n";
    $email_message .= "Name: $name\n";
    $email_message .= "Email: $email\n";
    $email_message .= "Subject: $subject\n";
    $email_message .= "Message:\n$message";

    // Additional email headers
    $headers = "From: $email\n";
    $headers .= "Reply-To: $email\n";

    // Send the email
    if (mail($to, $email_subject, $email_message, $headers)) {
        // Email sent successfully
        echo "Thank you for contacting us! We will get back to you soon.";
    } else {
        // Email sending failed
        echo "Oops! Something went wrong. Please try again later.";
    }
} else {
    // Redirect to the contact page if accessed directly
    header("Location: contact.html");
}
?>
