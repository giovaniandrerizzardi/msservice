
/////////////////////////////////
// Global 

var loc = window.location;
var ws;
var wsUri = "ws:";
var map;
var markers = [];
 var contentString = '<div id="content">'+
      '<div id="siteNotice">'+
      '</div>'+
      '<h1 id="firstHeading" class="firstHeading">Uluru</h1>'+
      '<div id="bodyContent">'+
      '<p><b>Uuid: </b> 15 </p>' +
      '<p><b>Uuid: </b> 15 </p>' +
      '<p><b>Uuid: </b> 15 </p>' +
      '<p><b>Uuid: </b> 15 </p>' +
      '<p><b>Uuid: </b> 15 </p>' +
      '</div>'+
      '</div>';

if (loc.protocol === "https:") { wsUri = "wss:"; }
// This needs to point to the web socket in the Node-RED flow
// ... in this case it's ws/simple
wsUri += "//" + loc.host + loc.pathname.replace("monitor","ws/alert");

//////////////////////////////////////////////
//  google map

function initMap() {
    map = new google.maps.Map(document.getElementById('map'), {
          zoom: 13,
          center: {lat: -28.26278, lng: -52.40667}
    });
}

/*
 msg.payload = {
    addr : 'Casa do seu Arlindo',
    uuid: 'uuid',
    la : -28.28278,
    lo : -52.40667,
    type : 'alertaST',
    severity : 1
  };


  {
    "uuid": "qweryy",
    "event_type": "sdff",
    "energy_ativa": "sd",
    "voltage_real_rms": "sddd",
    "phase_real_rms": "f",
    "lat": "1234",
    "lon": "12432"
}
*/

function dropCasa(type, addr, la, lo, uuid, event_type, energy_ativa, voltage_real_rms, phase_real_rms, alert_info) {
    
    clearMarker(addr);
    var marker;
    var infowindow;
    if (type === 'alerta') {
        marker = new google.maps.Marker({
        position: {lat: la, lng: lo},
        title : addr,
        map: map,
        label : 'A',
        animation: google.maps.Animation.DROP
        });
    } else {    
        marker = new google.maps.Marker({
        position: {lat: la, lng: lo},
        title : addr,
        map: map,
        label : 'G',
        animation: google.maps.Animation.DROP
        });    
    }

    var contentStringData = '<div id="content">' +
        '<div id="siteNotice">' +
        '</div>' +
        '<h1 id="firstHeading" class="firstHeading">Uluru</h1>' +
        '<div id="bodyContent">' +
        '<p><b>Uuid: </b> 15 </p>' +
        '<p><b>Uuid: </b> 15 </p>' +
        '<p><b>Uuid: </b> 15 </p>' +
        '<p><b>Uuid: </b> 15 </p>' +
        '<p><b>Uuid: </b> 15 </p>' +
        '</div>' +
        '</div>';


    
    infowindow = new google.maps.InfoWindow({
        content: contentString
    });
    
    marker.addListener('click', function() {
    infowindow.open(map, marker);
    });
    
    markers.push(marker);
}






function dropMarker (type, addr, la, lo) {
    
    clearMarker(addr);
    var marker;
    var infowindow;
    if (type === 'alertaST') {
        marker = new google.maps.Marker({
        position: {lat: la, lng: lo},
        title : addr,
        map: map,
        label : 'A',
        animation: google.maps.Animation.DROP
        });
    } else {
        marker = new google.maps.Marker({
        position: {lat: la, lng: lo},
        title : addr,
        map: map,
        label : 'G',
        animation: google.maps.Animation.DROP
        });    
    }
    
    infowindow = new google.maps.InfoWindow({
        content: contentString
    });
    
    marker.addListener('click', function() {
    infowindow.open(map, marker);
    });
    
    markers.push(marker);
}




function clearMarkers() {
    for ( var i = 0; i < markers.length; i++) {
        markers[i].setMap(null);
    }
}

function clearMarker(addr) {
    for ( var i = 0; i < markers.length; i++) {
        if ( markers[i].title == addr ) markers[i].setMap(null);
    }
}

////////////////////////////////////////////////
// Toastr

function showToast(type, addr, la, lo) {  
    toastr.options.positionClass = 'toast-bottom-full-width';    toastr.options.extendedTimeOut = 0; //1000;
    toastr.options.timeOut = 10000;
    toastr.options.fadeOut = 250;
    toastr.options.fadeIn = 250;
    var msg = ' Address : ' + addr;
    msg = msg + ', Latitude : '+ la;
    msg = msg + ', Longitude : '+ lo;
        
    if ( type === 'alertaST') {
        toastr.warning('<b>Alerta oObre tensão</b> '+msg);
    } else {
        toastr.error('<b>Alerta</b> '+msg);
    }
}

/////////////////////////////////////////////////
//adição da info windows




///////////////////////////////////////////////
// WebSocket 

function wsConnect() {
    
    console.log("connect",wsUri);
    ws = new WebSocket(wsUri);

    ws.onopen = function() {
       console.log("connected");
    }
    ws.onclose = function() {
        setTimeout(wsConnect,5000);
    }
    
    ws.onmessage = function(msg) {
        var payload = JSON.parse(msg.data);
        //console.log(payload);
        showToast(payload.type, payload.addr, payload.la, payload.lo);
        //insert Marker
        dropMarker(payload.type, payload.addr, payload.la, payload.lo);
    }
}

function action(m) {
    // Nothing has been defined yet
    if (ws) { ws.send(m); }
}
 
