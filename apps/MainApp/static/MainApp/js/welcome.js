//DROP DOWN MENU FOR TABLET MODE
function myFunction() {
    document.getElementById("tabletDropdown").classList.toggle("show");
  }
  
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

// $(document).on('submit', '')

// $('#joinButton').click(function() {
//   $.ajax({
//     url: 'Join',
//     method: 'POST',
//     success: function(response) {
//       console.log(response);
//     }
//   });
//   return false;
// })