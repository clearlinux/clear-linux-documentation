jQuery(document).ready(function($){

  var classItem = $('.custom-dropdown-menu li.parent-item').attr('class');
  if(classItem == 'menu-item-open parent-item') {
    $('.custom-dropdown-menu li.parent-item a').append('<span class="fa fa-chevron-down"></span>');
  } else {
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

  $('#block-menu-menu-social-media, #block-menu-menu-get-involved').click(function(){
    $(this).find('.menu').slideToggle();
  });

  $('.custom-dropdown-menu li.parent-item .fa').click(function(evt){
   evt.stopPropagation();
   $(this).toggleClass('fa-chevron-up fa-chevron-down');
   $(this).closest('li').toggleClass('menu-item-closed menu-item-open');
   return false;
  });

  $('div[id^=heading-]').click(function(){
    var section = $(this).attr('id').replace('heading-', '');
    $('#collapse-' + section).slideToggle();
    $('#title-'+ section +' a i').toggleClass('fa-plus-square fa-minus-square');
  });

  $('header .mobile-menu').click(function(){
    $('header').toggleClass('menu-open');
    $('.o1-logo-container-mobile').toggleClass('menu-open');
    $('body').toggleClass('menu-opened');
  });

  $('footer .mobile-menu').click(function(){
    $(this).parent().toggleClass('menu-open');
  });

  $('div[id^=heading-]').click(function(){
    var section = $(this).attr('id').replace('heading-', '');
    $('#collapse-' + section).slideToggle();
    $('#title-'+ section +' a i').toggleClass('fa-plus-square fa-minus-square');
  });

  function onScroll(el) {
    var $header = $('.project-header').first();
    var scrollTop = $(el.currentTarget).scrollTop();

    if (!$header.hasClass('scrolled') && scrollTop >= 200) {
      $header.addClass('scrolled');
    }

    if ($header.hasClass('scrolled') && scrollTop < 200) {
      $header.removeClass('scrolled');
    }
  }

  //Hidde mobile menu
  $(window).resize(function(event) {
    var w = $(window).width();
    if(w > 1199) {
      $('header').removeClass('menu-open');
    }
  });
  //Animates logo on scroll
  $('body, html').scroll(onScroll);
  $(window).scroll(onScroll);

});
