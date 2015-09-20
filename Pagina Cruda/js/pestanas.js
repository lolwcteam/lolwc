$(document).ready(function() {
    $(".hidden_Div").hide();
    $("#tabs-1").show();
})

function tab(tab){
    numTab=tab.value;
    $(".hidden_Div").hide();
    $("#tabs-"+numTab).show();
}