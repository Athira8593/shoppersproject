
(function(){
	if(typeof _bsa !== 'undefined' && _bsa) {
  		// format, zoneKey, segment:value, options
  		_bsa.init('flexbar', 'CKYI627U', 'placement:w3layoutscom');
  	}
})();


(function(){
if(typeof _bsa !== 'undefined' && _bsa) {
	// format, zoneKey, segment:value, options
	_bsa.init('fancybar', 'CKYDL2JN', 'placement:demo');
}
})();


(function(){
	if(typeof _bsa !== 'undefined' && _bsa) {
  		// format, zoneKey, segment:value, options
  		_bsa.init('stickybox', 'CKYI653J', 'placement:w3layoutscom');
  	}
})();



window.dataLayer = window.dataLayer || [];
  function gtag(){dataLayer.push(arguments);}
  gtag('js', new Date());

  gtag('config', 'UA-149859901-1');


     window.ga=window.ga||function(){(ga.q=ga.q||[]).push(arguments)};ga.l=+new Date;
     ga('create', 'UA-149859901-1', 'demo.w3layouts.com');
     ga('require', 'eventTracker');
     ga('require', 'outboundLinkTracker');
     ga('require', 'urlChangeTracker');
     ga('send', 'pageview');



      $(document).ready(function () {
        $(".button-log a").click(function () {
          $(".overlay-login").fadeToggle(200);
          $(this).toggleClass('btn-open').toggleClass('btn-close');
        });
      });
      $('.overlay-close1').on('click', function () {
        $(".overlay-login").fadeToggle(200);
        $(".button-log a").toggleClass('btn-open').toggleClass('btn-close');
        open = false;
      });


      $('#customerhnyCarousel').carousel({
          interval: 5000
      });

       transmitv.render();
  
       transmitv.cart.on('transmitv_checkout', function (evt) {
           var items, len, i;
  
           if (this.subtotal() > 0) {
               items = this.items();
  
               for (i = 0, len = items.length; i < len; i++) {}
           }
       });




  $(document).ready(function () {
      $('.popup-with-zoom-anim').magnificPopup({
        type: 'inline',
        fixedContentPos: false,
        fixedBgPos: true,
        overflowY: 'auto',
        closeBtnInside: true,
        preloader: false,
        midClick: true,
        removalDelay: 300,
        mainClass: 'my-mfp-zoom-in'
      });
  
    });



	$(function () {
      $('.navbar-toggler').click(function () {
        $('body').toggleClass('noscroll');
      })
    });
  

    // single view


(function(){
	if(typeof _bsa !== 'undefined' && _bsa) {
  		// format, zoneKey, segment:value, options
  		_bsa.init('flexbar', 'CKYI627U', 'placement:w3layoutscom');
  	}
})();


(function(){
if(typeof _bsa !== 'undefined' && _bsa) {
	// format, zoneKey, segment:value, options
	_bsa.init('fancybar', 'CKYDL2JN', 'placement:demo');
}
})();


(function(){
	if(typeof _bsa !== 'undefined' && _bsa) {
  		// format, zoneKey, segment:value, options
  		_bsa.init('stickybox', 'CKYI653J', 'placement:w3layoutscom');
  	}
})();


window.dataLayer = window.dataLayer || [];
  function gtag(){dataLayer.push(arguments);}
  gtag('js', new Date());

  gtag('config', 'UA-149859901-1');

    window.ga=window.ga||function(){(ga.q=ga.q||[]).push(arguments)};ga.l=+new Date;
    ga('create', 'UA-149859901-1', 'demo.w3layouts.com');
    ga('require', 'eventTracker');
    ga('require', 'outboundLinkTracker');
    ga('require', 'urlChangeTracker');
    ga('send', 'pageview');




    
    $.validator.addMethod("alpha", function(value, element) {
      return this.optional(element) || value == value.match(/^[a-zA-Z\s]+$/);
      // --                                    or leave a space here ^^
  });
  
  jQuery.validator.addMethod("noSpace", function(value, element) {
      return value == '' || value.trim(' ').length >=4;
    }, "Enter four characters");
  
  //ajax call
  
  
  $(document).ready(function (e) {
          $("#form").validate({
              rules:{
                  username:{
  
                      required:true,
                      minlength:4,
                      alpha: true,
                      noSpace: true,
                  },
                  password:{
  
                      required:true,
                      minlength:4,
                      alpha: true,
                      noSpace: true,
                  },
  
              },
              
          })
  
      })




      