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

$(document).ready(function() {
    $('.faq_question').click(function() {
       if ($(this).parent().is('.open')) {
          $(this).closest('.faq').find('.faq_answer_container').slideUp();
          $(this).closest('.faq').removeClass('open');
       } else {
          $('.faq_answer_container').slideUp();
          $('.faq').removeClass('open');
          $(this).closest('.faq').find('.faq_answer_container').slideDown();
          $(this).closest('.faq').addClass('open');
       }
    });
 }); 
 document.querySelectorAll('.smooth-scroll').forEach(anchor => {
    anchor.addEventListener('click', function(e) {
        e.preventDefault();

        const targetId = this.getAttribute('href').substring(1);
        const targetElement = document.getElementById(targetId);

        window.scrollTo({
            top: targetElement.offsetTop,
            behavior: 'smooth'
        });
    });
});
let prevScrollPos = window.scrollY;

window.addEventListener('scroll', () => {
    const currentScrollPos = window.scrollY;

    if (prevScrollPos > currentScrollPos) {
        // User is scrolling up, show navbar
        document.querySelector('.navbar').style.top = '0';
    } else {
        // User is scrolling down, hide navbar
        document.querySelector('.navbar').style.top = '-70px'; // Adjust the height as needed
    }

    prevScrollPos = currentScrollPos;
});

document.addEventListener('DOMContentLoaded', function () {
    AOS.init({
        duration: 800, 
        once: true,
        offset: 100, 
        easing: 'ease',
    });
});
