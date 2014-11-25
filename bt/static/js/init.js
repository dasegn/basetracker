(function($, window) {
    $('#side-menu').metisMenu();

    // Initializing tooltips
    $('[data-toggle="tooltip"]').tooltip();

    // Initializing popovers
    $('[data-toggle="popover"]').popover();

    $('.trigger-sidebar').on( 'click', function () {
        if ($('.sidebar-right').length) {
            if ($('.sidebar-right').hasClass('open')) {
                $('.sidebar-right').removeClass('open');
                $('.navbar').removeClass('sidebar-open');
                $('body').removeClass('menu-hidden');
            } else {
                $('body').addClass('menu-hidden');
                $('.sidebar-right').addClass('open');
                $('.navbar').addClass('sidebar-open');
            }
        }
    });

    $('.navbar-toggle').on('click', function () {
        if ($('#menu.hidden-xs').length)
            $('#menu').removeClass('hidden-xs');
        else
            $('#menu').addClass('hidden-xs');
    });
    
    //Loads the correct sidebar on window load
    $(window).bind("load", function() {
        if ($(this).width() < 768) {
            $('div.sidebar-collapse').addClass('collapse')
        } else {
            $('div.sidebar-collapse').removeClass('collapse')
        }
    });


    //Collapses the sidebar on window resize
    $(window).bind("resize", function() {
        if ($(this).width() < 768) {
            $('div.sidebar-collapse').addClass('collapse')
        } else {
            $('div.sidebar-collapse').removeClass('collapse')
        }
    });



    // Adding niceScroll to HTML tag
    $( "html" ).niceScroll({cursorcolor: 'green', cursorborder: "none", horizrailenabled: false, zindex: 2000 });

    $('.has-nice-scroll').each(function () {
        $(this).niceScroll({
            horizrailenabled: false, 
            zindex: 2000,
            cursorborder: "none",
        });
    });

    // Stopping Dropdown menu from closing on click event
    $('.mega-menu .dropdown-menu').on('click', function (event) {
        event.stopPropagation();
    });



    // removing panels
    $('[data-action^="close"]').on('click', function () {
      $(this).closest('.panel').hide();
    });

    // realoding panels
    $('[data-action^="reload"]').on('click', function () {
      $(this).closest(".panel").children('.panel-body').block({ 
        message: '<h2><i class="fa fa-spinner fa-spin"></i></h2>',
        css: { 
          border: 'none', 
          padding: '15px', 
          background: 'none',
        },
        overlayCSS: { backgroundColor: '#FFF' },
        timeout: 2000 
      });
    });
    // panle settings
    $('[data-action^="settings"]').on('click', function () {

    });
    // panle minimize
    $('[data-action^="minimize"]').on('click', function () {
      if ($(this).hasClass('active')){
        $(this).removeClass('active');
        $(this).closest(".panel").children('.panel-body').slideDown('fast'); 
      } else{
        $(this).addClass('active');
        $(this).closest(".panel").children('.panel-body').slideUp('fast'); 
      }
    });

})(jQuery, window);