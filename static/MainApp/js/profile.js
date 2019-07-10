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

// $(document).ready(function() {
//   // THE BELOW GETS THE COOKIES FOR THE CSRF TOKEN, THAT IS REQUIRED FOR THE FORM TO ALLOW AJAX TO PASS THE ID VALUE!!!
//   function getCookie(name) {
//       var cookieValue = null;
//       if (document.cookie && document.cookie !== '') {
//           var cookies = document.cookie.split(';');
//           for (var i = 0; i < cookies.length; i++) {
//               var cookie = cookies[i].trim();
//               // Does this cookie string begin with the name we want?
//               if (cookie.substring(0, name.length + 1) === (name + '=')) {
//                   cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
//                   break;
//               }
//           }
//       }
//       return cookieValue;
//   }
      
//   var csrftoken = getCookie('csrftoken');

//   // CREATES CSRF FUNCTION TO BE CALLED IN AJAX SETUP!!!
//   function csrfSafeMethod(method) {
//       return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
//   }

//   // AJAX SETUP FOR CSRF TOKEN TO BE PASSED FOR AJAX TO RUN!!
//   $.ajaxSetup({
//       beforeSend: function(xhr, settings) {
//           if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
//               xhr.setRequestHeader("X-CSRFToken", csrftoken);
//           }
//       }
//   });   

//   // THE '.off' PREVENTS AJAX FROM RUNNING FORM MULTIPLE TIMES!!!
//   $(function() {
//   $('#Cancel').click(function() { 
//       $(document).off('submit', '#CancelButton');
//       $(document).on('submit', '#CancelButton', function(event) {
//           event.preventDefault();
//         });

//           // AJAX CALL TO SUBMIT FORM!!
//           $.ajax({
//                method: 'POST',
//               url: $(this).attr('action'),
//               data: $(this).serialize(),
//               success: 
//                   alert('YOU ARE NO LONGER ATTENDING --- {{event.Title}} ---')
//           });
//         $('#CancelButton').submit();
//         return false;
//   });
// });


// });

// $('#CancelButtonForm').submit(function() {
//   console.log('******************IM HERE******************')
//   $.ajax({
//       method: "POST",
//       url: $(this).attr('action'),
//       data: $(this).serialize(),
//       success: function(response) {
//         alert("******************")
//         console.log(url)
//       }
//   })
//   return false;
// });