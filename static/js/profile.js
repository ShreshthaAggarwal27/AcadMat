// profile.js

// Function to show content sections based on the clicked link
function showContent(sectionId) {
    const contentSections = document.querySelectorAll(".content-section");

    // Hide all content sections
    contentSections.forEach(function (section) {
        section.style.display = "none";
    });

    // Show the selected content section
    const selectedSection = document.getElementById(sectionId);
    if (selectedSection) {
        selectedSection.style.display = "block";
    }
}

// Show the Personal Details section by default
showContent("personal-details");