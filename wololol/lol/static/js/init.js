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
    });
})(jQuery);