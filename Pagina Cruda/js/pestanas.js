$(document).ready(function() {
    $(".hidden_Div").hide();
    $("#tabs-2").show();
})

function tab(tab){
    numTab=tab.value;
    $(".hidden_Div").hide();
    $(".tab").removeClass("pestana_opciones_active")
    $(tab).addClass("pestana_opciones_active");
    $("#tabs-"+numTab).show();
}
