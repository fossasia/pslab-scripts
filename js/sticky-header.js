$(document).ready(function(){
	var stickyNavTop = $('#sticky-navbar').offset().top;
	 
	var stickyNavBar = function(){
	var scrollTop = $(window).scrollTop();
	      
	if (scrollTop > stickyNavTop) { 
	    $('#sticky-navbar').addClass('sticky');
	} else {
	    $('#sticky-navbar').removeClass('sticky'); 
	}

	if (scrollTop > 540) { 
	    $('#sticky-navbar').addClass('sticked');
	} else {
	    $('#sticky-navbar').removeClass('sticked'); 
	}
	};
	 
	stickyNavBar();
	 
	$(window).scroll(function() {
	  stickyNavBar();
	});
});