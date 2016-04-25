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

  $('header .mobile-menu').click(function(){
    $(this).parent().toggleClass('menu-open');
    $('.o1-logo-container-mobile').toggleClass('menu-open');
    $('body').toggleClass('menu-opened');
  });

  $('footer .mobile-menu').click(function(){
    $(this).parent().toggleClass('menu-open');
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

  $('#block-menu-menu-social-media, #block-menu-menu-get-involved').click(function(){
    $(this).find('.menu').slideToggle();
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

  //Animates logo on scroll
  $('body, html').scroll(onScroll);
  $(window).scroll(onScroll);

  if (!$('html').hasClass('cssanimations') && $('body').hasClass('front')) {
    margin = [0, -37, -74, -111],
    i = 0,
    tickerNewsInterval = tickerNews();

    $('.pane-news-panel-pane-news-ticker .view-content').hover(function(){
      clearInterval(tickerNewsInterval);
    });

    $('.pane-news-panel-pane-news-ticker .view-content').mouseleave(function(){
      tickerNewsInterval = tickerNews();
    });
  }

  function tickerNews(){
    return setInterval(function(){
      i = (i + 1 < 4) ? i + 1 : 0;
      $('.pane-news-panel-pane-news-ticker .view-content').stop(true).animate({
        marginTop: margin[i] + 'px'
      }, 1000);
    }, 2500);
  }
});
