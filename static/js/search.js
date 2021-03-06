var isSearchLandingPage = (window.location.pathname == '/search/' && window.location.search == '');

$(window).on('load', function() {
    
    $("#loader").delay(1000).fadeOut("fast", function() {

        $("#cocktailSection, #search_results, #loadremaining, #search_hint").fadeIn("slow");
        
        //console.log(isSearchLandingPage);

        //For '/search/' GET request as a demo of flipped card with autofocus (1/2) afterwards
        if (isSearchLandingPage) {
            //Demo flip animation. Timeout is required as js doesnt know when the animation has ended
            function flip() {
                $('#1_container').toggleClass('flipped');
            }

            setTimeout(
                function() { flip(
                    setTimeout(
                        function(){ flip(
                            setTimeout(
                                function(){ $('#cocktailSection').fadeOut("slow", 
                                    function() {
                                        $('#demo_search_hint').fadeIn("slow");
                                        //Clicking on the search hint gives focus to the searchbar
                                        $('#demo_search_hint').on('click', function() {
                                            
                                            if (window.screen.availWidth >= 769) {
                                                $('#nav_search_input').focus();
                                                // console.log('LARGER NAV');
                                            } else {
                                                $('#page_search_input').focus();
                                                // console.log('SMALLER NAV');
                                            }
                                             
                                        });
                                    }
                                )}
                            , 1000) //Fadeout
                        )}
                    , 1000) //Reverse flip
                )}
            , 1000); //Initial flip
            
        }
        
        //Autofocus (2/2): Clicking on the search hint gives focus to the searchbar
        $("[name='error_message']").on('click', function() {
            if (window.screen.availWidth >= 769) {
                $('#nav_search_input').focus();
                // console.log('LARGER NAV');
            } else {
                $('#page_search_input').focus();
                // console.log('SMALLER NAV');
            }
        });
        
        // Scrolling to where we were last when loading all items by looking at html meta data
        if ($("#all_items").attr("value") == 'true') {
            window.scrollTo(0, 1028);
            
        }
    });
});

$(document).ready(function() {

    //Enables ALL interactivity for the search page (ajax etc.)
    //Disables interactivity for the demosession
    if (!isSearchLandingPage) {

        // TOGGLE FLIP CARDS
        $(".outer-container-flip").on('click', function(){
            
            card_id = this.id;
            console.log(card_id)
            
            $('#' + card_id).toggleClass('flipped');
        
        });

        let empty = "far fa-heart card-badge";
        let full = "fas fa-heart card-badge";
        let none = "far fa-heart card-badge ";

        $("[name='favorite']").on('click', function(event){

            var drink_id;
            drink_id = $(this).attr('id');

            if (this.className === empty) {
                ajax_update_fav(drink_id, 'add');
                
            } else if (this.className === full) {
                ajax_update_fav(drink_id, 'remove');
                //this.className = empty;
            } else if (this.className === none) {
                // $('#' + drink_id).popover('enable').popover('show');
                //console.log('#' + drink_id + '_favorite')
                alert('Please log in to add to favorites');
            }

            //Below is needed so that the card is not flipped after pressing the favorite icon
            event.stopImmediatePropagation();
        });

        function toggle_favloader(callback_type, drink_id, update_type) {
                
            if (callback_type == 'success') {

                if (update_type == 'add') {
                    setTimeout(function() {$('#' + drink_id + '_favorite_loader').fadeOut('slow')}, 300);
                    setTimeout(function() {$('#' + drink_id).removeClass().addClass('fas fa-heart card-badge').fadeIn('slow')}, 800);
                } else if (update_type == 'remove') {
                    setTimeout(function() {$('#' + drink_id + '_favorite_loader').fadeOut('slow')}, 300);
                    setTimeout(function() {$('#' + drink_id).removeClass().addClass('far fa-heart card-badge').fadeIn('slow')}, 800);
                }

            } else if (callback_type == 'error') {

                //restoring the original class
                if (update_type == 'add') {
                    setTimeout(function() {$('#' + drink_id + '_favorite_loader').fadeOut('slow')}, 300);
                    setTimeout(function() {$('#' + drink_id).removeClass().addClass('far fa-heart card-badge').fadeIn('slow')}, 800);
                } else if (update_type == 'remove') {
                    setTimeout(function() {$('#' + drink_id + '_favorite_loader').fadeOut('slow')}, 300);
                    setTimeout(function() {$('#' + drink_id).removeClass().addClass('fas fa-heart card-badge').fadeIn('slow')}, 800);
                }
                
                setTimeout(function() {alert('Connection issue. Please try again later')}, 1000);

            } else {
                //Clearing the badge icon and loading the animation
                $('#' + drink_id).removeClass().addClass('card-badge');
                $('#' + drink_id + '_favorite_loader').show();
                $('#' + drink_id + '_favorite_loader').fadeIn('slow');   
            }
 
        }

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
            console.log('#' + drink_id);
            toggle_favloader('',drink_id);

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
                        console.log('Success. Server message: ' + data);
                        // Updating the visual
                        toggle_favloader('success', drink_id, update_type);
                    },
                    error: function ( data )
                    {
                        console.log('Error. Server message: ' + data);
                        // Updating the visual
                        toggle_favloader('error', drink_id, update_type);
                    }
                })

        };

};

});