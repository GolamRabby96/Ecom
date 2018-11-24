
$('.go-top').hide();

$(window).scroll(function(){
	var jkono = $(this).scrollTop();
	$('.abc').html(jkono);

	if( jkono<500){
		$('.go-top').fadeOut(1000);
	} else {
		$('.go-top').fadeIn(1000);
	}

});

$(document).ready(function(){
	$('.go-top').click(function(){
		$('body, html').animate({scrollTop: 0},500);
	});
});

$(function () {
  $('[data-toggle="tooltip"]').tooltip()
})

$(function () {
  $('[data-toggle="popover"]').popover()
})





$(document).ready(function() {
	var s = $(".navbar-fixed-top");
	var pos = s.position();					   
	$(window).scroll(function() {
		var windowpos = $(window).scrollTop();
		if (windowpos >= pos.top & windowpos >700) {
            s.addClass("navbar-fixed-top");
		} else {
            s.removeClass("navbar-fixed-top"),500;	
		}
	});
});