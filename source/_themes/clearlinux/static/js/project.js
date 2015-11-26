jQuery(document).ready(function($){
	var classItem = $('.custom-dropdown-menu li.parent-item').attr('class');
	if(classItem == 'menu-item-open parent-item'){
		$('.custom-dropdown-menu li.parent-item a').append('<span class="fa fa-chevron-down"></span>');
	}
	else{
		$('.custom-dropdown-menu li.parent-item a').append('<span class="fa fa-chevron-up"></span>');
	}


	$('header .mobile-menu').click(function(){
		$(this).parent().toggleClass('menu-open');
		$('.o1-logo-container-mobile').toggleClass('menu-open');
		$('body').toggleClass('menu-opened');
	});

	$('footer .mobile-menu').click(function(){
		$(this).parent().toggleClass('menu-open');
	});

	$('.custom-dropdown-menu li.parent-item .fa').click(function(evt){
		evt.stopPropagation();
		$(this).toggleClass('fa-chevron-up fa-chevron-down');
		$(this).closest('li').toggleClass('menu-item-closed menu-item-open');
		return false;
	});

	$('.faq-question').click(function(){
		$(this).toggleClass('opened');
		$(this).next().toggleClass('opened');
	});

	$('div[id^=heading-]').click(function(){
		var section = $(this).attr('id').replace('heading-', '');
		$('#collapse-' + section).slideToggle();
		$('#title-'+ section +' a i').toggleClass('fa-plus-square fa-minus-square');
	});
});
