document.addEventListener('DOMContentLoaded', function() {
    const toggleButton = document.getElementById('toggleCategories');
    const showMoreButton = document.getElementById('showMoreContainer');
    const showLessButton = document.getElementById('showLessContainer');
    const additionalCategories = document.getElementById('additionalCategories');
    const toggleIconSpan = document.getElementById('toggleIcon');
    const categories = document.getElementById("categoriesContainer");
    const dateFilterCheckboxes = document.querySelectorAll('input[name="dateFilter"]');
    const bookCards = document.querySelectorAll('.book-card');

    function toggle() {
        if (categories.style.display === '' || categories.style.display === 'block') {
            toggleIconSpan.style.transform = "rotate(90deg)";
            categories.style.display = 'none';
        } else {
            toggleIconSpan.style.transform = "rotate(0deg)"; 
            categories.style.display = 'block';
        }
    }
    
    function toggleCategories() {
        if (additionalCategories.style.display === 'none' || additionalCategories.style.display === '') {
            additionalCategories.style.display = 'block';
            showMoreButton.style.display = 'none';
            showLessButton.style.display = 'block';
        } else {
            additionalCategories.style.display = 'none';
            showLessButton.style.display = 'none';
            showMoreButton.style.display = 'block';
        }
    }

    showMoreButton.addEventListener('click', function(event) {
        event.preventDefault();
        toggleCategories();
    });

    showLessButton.addEventListener('click', function(event) {
        event.preventDefault();
        toggleCategories();
    });

    toggleButton.addEventListener('click', function(event) {
        event.preventDefault();
        toggleCategories();
    });

    toggleIconSpan.addEventListener('click', function(event) {
        event.preventDefault();
        toggle();
    });
});

function filterBooksByDate(days) {
    const currentDate = new Date();
    const cutoffDate = new Date();
    cutoffDate.setDate(currentDate.getDate() - days);

    bookCards.forEach(function (card) {
        const donatedDate = new Date(card.dataset.donatedDate);
        if (donatedDate >= cutoffDate) {
            card.style.display = 'block';
        } else {
            card.style.display = 'none';
        }
    });

    dateFilterCheckboxes.forEach(function (checkbox) {
        checkbox.addEventListener('change', function () {
            if (checkbox.checked) {
                const days = parseInt(checkbox.value);
                filterBooksByDate(days);
            } else {
                bookCards.forEach(function (card) {
                    card.style.display = 'block';
                });
            }
        });
    });
}
