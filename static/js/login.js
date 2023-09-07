document.addEventListener("DOMContentLoaded", function() {
    const form = document.getElementById("login-form");

    form.addEventListener("submit", function(event) {
        event.preventDefault();

        const username = document.getElementById("username").value;
        const password = document.getElementById("password").value;

        console.log("Username:", username);
        console.log("Password:", password);
    });
    const forgotPasswordLink = document.getElementById("forgot-password-link");
const resetForm = document.getElementById("reset-form");

forgotPasswordLink.addEventListener("click", function (event) {
    event.preventDefault();
    resetForm.classList.toggle("hidden");
});
document.getElementById("login-individual").addEventListener("click", function() {
    showLoginForm("individual");
});

document.getElementById("login-institution").addEventListener("click", function() {
    showLoginForm("institution");
});

function showLoginForm(type) {
    const loginFormContainer = document.getElementById("login-form-container");
    const loginChoice = document.querySelector(".choice");

    if (type === "individual" || type === "institution") {
        loginChoice.style.display = "none";
        loginFormContainer.classList.remove("hidden");

    }
}

});
