document.getElementById('login-button').addEventListener('click', function () {
    // Get form data
    const institutionName = document.getElementById('institutionName').value;
    const institutionEmail = document.getElementById('institutionEmail').value;
    const institutionPassword = document.getElementById('institutionPassword').value;

    // Validate form data (you can add more validation logic here)

    if (!institutionName || !institutionEmail || !institutionPassword) {
        alert('Please fill in all the fields.');
    } else {
        // Simulate form submission (replace this with actual form submission code)
        alert('Form submitted successfully.');
        // You can also use AJAX to submit the form data to a server.
    }
});
