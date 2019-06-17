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

  // $(document).on('submit', '#CancelButton', function(e) {
  //   e.preventDefault();

  //     $.ajax({
  //     type: 'POST',
  //     data: {
  //     url: '/RemoveProcess' + id,
  //     id: Event.objects.get(id=id)
  //     },


  //     success: function() {
  //         alert("No longer Attending");
  //     }
  //   });
  // });
}