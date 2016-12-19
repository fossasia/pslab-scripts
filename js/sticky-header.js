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
		$("#dark-logo").show();
		$("#light-logo").hide();
	    $('#sticky-navbar').addClass('sticked');
	} else {
		$("#dark-logo").hide();
		$("#light-logo").show();
	    $('#sticky-navbar').removeClass('sticked'); 
	}
	};

	if($( window ).width() > 776){
		$("#fossasia-link").hide();

	}else if($( window ).width() < 776){
		$("#fossasia-link").show();
		$("#light-logo").remove();
		$("#dark-logo").remove();
	}
	 
	stickyNavBar();
	 
	$(window).scroll(function() {
	  stickyNavBar();
	});
});