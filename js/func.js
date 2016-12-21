$(function(){
$(".navbar-collapse ul li a").click(function(){
    $(".navbar-toggle:visible").click();
  })
    $('a.page-scroll').bind('click', function(event) {
        var $anchor = $(this);
        $('html, body').stop().animate({
            scrollTop: ($($anchor.attr('href')).offset().top - 50)
        }, 1250);
        event.preventDefault();
    });
})
