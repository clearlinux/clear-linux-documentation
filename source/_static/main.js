jQuery(document).ready(function($) {
  $('body').fadeIn();
  var headerEffect = function(h, p) {
    p = p -60; // offset caused by header
    console.log("pos: " + p);
    var elements = [];
    elements.push($('img.logo-region-highlighted').position());
    elements.push($('div.region-homepage').position());
    elements.push($('footer').position());
    console.log(elements);
    if (p <= elements[0].top) {
      h.removeClass('-hidden -full-header');
    } else if (p > elements[0].top && p <= elements[1].top ){
      h.addClass('-hidden');
    } else if (p > elements[1].top && p <= elements[2].top ) {
      h.removeClass('-hidden');
      h.addClass('-full-header');
    }
  };
  var wrapper = $('div#wrapper');
  var mobileMenu = $('nav#main-menu-mobile');
  var mobileMenuBars = $('span#nav-bars');
  var searchButton = $('span#nav-search');
  var searchContainer = $('div#search-container');
  var overlayClass = '-overlay';

  if ($('body').hasClass('front')) {
    var currentPos = $(window).scrollTop();
    var header = $('header');
    headerEffect(header, currentPos);

    $(window).scroll(function() {
      var currentPos = $(window).scrollTop();
      console.log(currentPos);
      headerEffect(header, currentPos);
    });
  }

  var overlayBehavior = function(action) {
    cssClass = '-overlay';
  }
  var menuMobile = function(action) {
    
  }
  
  var resized =  false;
  $(window).resize(function() {
    console.log($(window).width());
    if ($(window).width() > 768 && !resized) {
      console.log('si');
      resized = true;
    } else {
      resized = false;
    }
  });

  mobileMenuBars.click(function() {
    body = $('body');
    if (mobileMenu.is(':visible')) {
      mobileMenu.slideUp();
      body.removeClass('-expanded-mobile-menu');
      if (!body.hasClass('-expanded-search-box')) {
        body.removeClass('-expanded-header');
        wrapper.removeClass(overlayClass);
      }
    } else {
      mobileMenu.slideDown();
      body.addClass('-expanded-header -expanded-mobile-menu');
      wrapper.addClass(overlayClass);
    }
  });
  
  // shows and hides the search text box
  searchButton.click(function() {
    if (searchContainer.is(':visible')) {
      searchContainer.slideUp();
      $('body').removeClass('-expanded-search-box');
      if (!$('body').hasClass('-expanded-mobile-menu')) {
        $('body').removeClass('-expanded-header');
        wrapper.removeClass(overlayClass);
      }
    } else {
      searchContainer.slideDown();
      $('body').addClass('-expanded-header -expanded-search-box');
      wrapper.addClass(overlayClass);
    }
  });

  var normalHeaderState = function() {
    body = $('body');
    if (body.hasClass('-expanded-header')) {
      if (searchContainer.is(':visible')) {
        searchContainer.slideUp()
        body.removeClass('-expanded-search-box');
      }
      if (mobileMenu.is(':visible')) {
        mobileMenu.slideUp();
        body.removeClass('-expanded-mobile-menu');
      }
      wrapper.removeClass(overlayClass);
      $('body').removeClass('-expanded-header');
    }
  }
  $('html').click(function() {
    normalHeaderState();
  });

  $('header').click(function(event){
    event.stopPropagation();
  });

  $('span#secondary-menu-button').click(function() {
    $('div.region-sidebar').slideToggle();
    $('div.container-sidebar').toggleClass('-expanded-submenu');
  });

  $(document).on('keyup', function(e) {
    if (e.keyCode == 27 && wrapper.hasClass('-overlay')) {
      normalHeaderState();
    }
  });
});
