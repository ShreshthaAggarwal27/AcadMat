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