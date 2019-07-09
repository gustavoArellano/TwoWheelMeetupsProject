var geocoder;
var map;

function initMap() {
    geocoder = new google.maps.Geocoder();

    // var latlng = new google.maps.LatLng(37.773972, -122.431297);

    var mapOptions = {
        zoom: 13,
        // center: latlng,
        scaleControl: false,
        fullscreenControl: false,
        zoomControl: true,
        mapTypeControl: false,
        streetViewControl: false
        }
    map = new google.maps.Map(document.getElementById('map'), mapOptions);
}

function codeAddress() {
    var address = document.getElementById('address').value;

    geocoder.geocode( { 'address': address}, function(results, status) {

        if (status == 'OK') {
            map.setCenter(results[0].geometry.location);

            var marker = new google.maps.Marker({
                map: map,
                position: results[0].geometry.location,
                animation: google.maps.Animation.DROP
                });
            
            var infowindow = new google.maps.InfoWindow({
                content:"<div class='infoWindow'><p><strong>We Meet Here!!!</strong></p>***SEE DESCRIPTION FOR DETAILS***</div>"
                });

            google.maps.event.addListener(marker, 'click', function() {
                infowindow.open(map,marker);
            });

            marker.addListener('click', toggleBounce);
            
            function toggleBounce() {
                if (marker.getAnimation() !== null) {
                    marker.setAnimation(null);
                } else {
                    marker.setAnimation(google.maps.Animation.BOUNCE);
                    setTimeout(function(){ marker.setAnimation(null); }, 750);
                }
            }
        } else {
            alert('Geocode was not successful for the following reason: ' + status);
        }
    });
}

