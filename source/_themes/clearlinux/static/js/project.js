jQuery(document).ready(function($){
	$('header .mobile-menu').click(function(){
		$(this).parent().toggleClass('menu-open');
		$('.o1-logo-container-mobile').toggleClass('menu-open');
		$('body').toggleClass('menu-opened');
	});

	$('footer .mobile-menu').click(function(){
		$(this).parent().toggleClass('menu-open');
	});

	$('.custom-dropdown-menu li .fa').click(function(evt){
		evt.stopPropagation();
		$(this).toggleClass('fa-angle-down fa-angle-up');
		$(this).closest('li').toggleClass('menu-item-open menu-item-closed');
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
