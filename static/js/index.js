var popup = document.getElementById("popup");
var popupInner = document.getElementById("popup-inner");
var popupClose = document.getElementById("popup-close");
var readMoreBtns = document.querySelectorAll(".read-more-btn");


readMoreBtns.forEach(function(btn) {
    btn.addEventListener("click", function() {
        
        popup.style.display = "block";

        var contentId = btn.getAttribute("data-content");
        var content = document.getElementById(contentId)

        popupInner.innerHTML = content.innerHTML;
    });
});

popupClose.addEventListener("click", function() {
    popup.style.display = "none";
});
var learnMoreBtns = document.querySelectorAll(".learn-more-btn");

learnMoreBtns.forEach(function(btn) {
    btn.addEventListener("click", function() {
        popup.style.display = "block";

        var contentId = btn.getAttribute("data-content");
        var content = document.getElementById(contentId);

        popupInner.innerHTML = content.innerHTML;
    });
});
