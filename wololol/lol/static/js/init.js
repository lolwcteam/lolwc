(function($){
    $(function(){
        $('.button-collapse').sideNav();
        $('.parallax').parallax();
        $('select').material_select();
        $('.datepicker').pickadate({
            selectMonths: true,
            selectYears: 15
        });
        $('.slider').slider({full_width: true});
        $('.materialboxed').materialbox();
        $('.modal-trigger').leanModal();
        $('.tooltipped').tooltip({delay: 50});
        $('.dropdown-button').dropdown({
            inDuration: 300,
            outDuration: 225,
            constrain_width: true, // Does not change width of dropdown to that of the activator
            hover: false, // Activate on hover
            gutter: 0, // Spacing from edge
            belowOrigin: false, // Displays dropdown below the button
            alignment: 'left' // Displays dropdown with edge aligned to the left of button
        }
                                      );        
    });
})(jQuery);