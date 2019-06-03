// Ready is needed because the js reference is placed at the top of the page (head)
$(document).ready(function() {

    // ADD SLIDE ANIMATIONS
    $(window).scroll(function() {
        $(".slideanim").each(function(){
            var pos = $(this).offset().top;

            var winTop = $(window).scrollTop();
            if (pos < winTop + 600) {
            $(this).addClass("slide");
            }
        });
    });

    // Smooth scroll hashes
    $("a").on('click', function(event) {

        // Make sure this.hash has a value before overriding default behavior
        if (this.hash !== "") {
          // Prevent default anchor click behavior
           event.preventDefault();
    
          // Store hash
          var hash = this.hash;
    
          // Using jQuery's animate() method to add smooth page scroll
          // The optional number (800) specifies the number of milliseconds it takes to scroll to the specified area
          $('html, body').animate({
            scrollTop: $(hash).offset().top
          }, 800, function(){
    
            // Add hash (#) to URL when done scrolling (default click behavior)
            window.location.hash = hash;
          });
        //   return false;
        } // End if
    });

    // Workaround for Safari when coming from a different page. It wouldn't simulate a scroll to trigger the animation
    if(window.location.hash) {
        window.scrollBy(0, 1);
    }

});