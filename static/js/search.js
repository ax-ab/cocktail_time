// Page preloader. 1800 is exactly the time it takes for the full animation to complete
$(window).on('load', function() {

    $("#loader").delay(1000).fadeOut("fast", function() {

        $("#cocktailSection, #search_results, #loadremaining_wrapper").fadeIn("slow");
        
        //For '/search/' GET request as a demo of flipped card
        if (window.location.pathname == '/search/' && window.location.search == '') {
            
            //Demo flip animation. Timeout is required as js doesnt know when the animation has ended
            function flip() {
                $('#1_container').toggleClass('flipped');
            }

            flip(
                setTimeout(
                    function(){ flip(
                        setTimeout(
                            function(){ $('#cocktailSection').fadeOut("slow", 
                                function() {
                                    $('#demo_search_hint').fadeIn("slow")
                                }
                            )}
                        , 1000)
                    )   }
                , 1000)
            );

        }
        // Scrolling to where we were last
        // console.log($("#all_items").attr("value"));
        if ($("#all_items").attr("value") == 'true') {
            window.scrollTo(0, 1028);

            // exact: 1028
            // new section: 1165

            // Below is not adding smooth scroll to be deleted
            // $('html, body').animate({
            // scrollTop: window.scrollTo(0, 1028)
            // }, 800);

            //DEBUGGING TO DETERMINE EACT POSITION
            // $(window).scroll(function (event) {
            //     var scroll = $(window).scrollTop();
            //     console.log(scroll);
            // });
            
        }
    });
});

// Ready is needed because the js reference is placed at the top of the page (head)
$(document).ready(function() {

    //Disables interactivity for the demosession
    if (!(window.location.pathname == '/search/' && window.location.search == '')) {

        // TOGGLE FLIP CARDS
        $(".outer-container-flip").on('click', function(){
            
            card_id = this.id;
            console.log(card_id)
            
            $('#' + card_id).toggleClass('flipped');
        
        });

        // TOGGLE FAVORITES
        // let empty = "fas fa-glass-martini-alt";
        // let full = "fas fa-glass-martini";

        let empty = "far fa-heart card-badge";
        let full = "fas fa-heart card-badge";
        let none = "far fa-heart card-badge ";

        $("[name='favorite']").on('click', function(event){

            var drink_id;
            drink_id = $(this).attr('id');

            console.log("id: " + drink_id);
            console.log("class: " + $(this).attr('class'));
            console.log("name: " + $(this).attr('name'));

            if (this.className === empty) {
                ajax_update_fav(drink_id, 'add')
                
            } else if (this.className === full) {
                ajax_update_fav(drink_id, 'remove')
                //this.className = empty;
            } else if (this.className === none) {
                // $('#' + drink_id).popover('enable').popover('show');
                //console.log('#' + drink_id + '_favorite')
                alert('Please log in to add to favorites')
            }

            //Below is needed so that the card is not flipped after pressing the favorite icon
            event.stopImmediatePropagation();
        });

        //CSRF function and setup for ajax post request.
        function csrfSafeMethod(method) {
            // these HTTP methods do not require CSRF protection
            return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
        }
        $.ajaxSetup({
            beforeSend: function(xhr, settings) {
                if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
                    xhr.setRequestHeader("X-CSRFToken", csrftoken);
                }
            }
        });

        var csrftoken = jQuery("[name=csrfmiddlewaretoken]").val();

        function ajax_update_fav(drink_id, update_type) 
        {
            $.ajax
            ({
                type: "POST",
                url: "../update_favorites/",
                data:{
                        drink_id:drink_id,
                        update_type:update_type                          
                },
                success: function ( data )
                {
                    // Reply from Django
                    console.log('Django: ' + data) 
                    // Updating the visual
                    if (update_type === 'add') {
                        $('#' + drink_id).removeClass().addClass('fas fa-heart card-badge');
                    } else if (update_type === 'remove') {
                        $('#' + drink_id).removeClass().addClass('far fa-heart card-badge');
                    }            
                }
            })
        }

}

});