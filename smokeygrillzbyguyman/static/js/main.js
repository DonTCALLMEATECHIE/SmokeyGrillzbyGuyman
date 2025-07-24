// Contact Form (Fake AJAX)
function submitContactForm(e) {
    e.preventDefault();
    document.getElementById('contact-result').textContent = "Thanks for reaching out! We'll get back to you soon.";
    document.getElementById('contact-form').reset();
}