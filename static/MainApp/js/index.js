$(document).ready(function() {
    $(".eventInfo h3").text(function(index, currentText) {
        return currentText.substr(0, 15) + "...";
    });
});