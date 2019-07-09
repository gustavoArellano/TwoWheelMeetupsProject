//DROP DOWN MENU FOR TABLET MODE
function myFunction() {
    document.getElementById("tabletDropdown").classList.toggle("show");
  
  window.onclick = function(event) {
    if (!event.target.matches('.menuButton')) {
      var dropdowns = document.getElementsByClassName("dropdown-content");
      var i;
      for (i = 0; i < dropdowns.length; i++) {
        var openDropdown = dropdowns[i];
        if (openDropdown.classList.contains('show')) {
          openDropdown.classList.remove('show');
        }
      }
    }
  }
}

// AJAX COMMAND FOR SEARCH
function searchEvent() {
  $('.myForm').click(function(e){
    e.preventDefault()
  });

  $('#AjaxStartsWithButton').click(function() {
    $.ajax({
        url: "/Explore/Api",
        method: "POST",
        data: $(this).parent().serialize(), 
            success: function(serverResponse) { 
                $('#list').html(serverResponse)
            }
    });
  });
};