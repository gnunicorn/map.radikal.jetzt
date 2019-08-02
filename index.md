---
# Feel free to add content and custom Front Matter to this file.
# To modify the layout, see https://jekyllrb.com/docs/themes/#overriding-theme-defaults

layout: map
---

<link rel="stylesheet" href="/assets/leaflet.css" />
<link rel="stylesheet" href="/assets/css/easy-button.css" />
<link rel="stylesheet" href="/assets/css/L.Control.Locate.min.css" />
<link rel="stylesheet" href="/assets/css/all.css" />
<link rel="stylesheet" href="/assets/css/leaflet-sidebar.min.css" />


<div id="mapid" class="sidebar-map"></div>
<div id="sidebar" class="sidebar collapsed">
    <!-- Nav tabs -->
    <div class="sidebar-tabs">
        <ul role="tablist">
            <li><a href="#filter" role="tab"><i class="fa fa-filter"></i></a></li>
        </ul>

        <ul role="tablist">
            <li><a href="#info" role="tab"><i class="fa fa-info"></i></a></li>
            <li class="disabled"><a href="#messages" role="tab"><i class="fa fa-envelope"></i></a></li>
            <li><a href="#settings" role="tab"><i class="fa fa-github"></i></a></li>
        </ul>
    </div>

    <!-- Tab panes -->
    <div class="sidebar-content">
        <div class="sidebar-pane" id="filter">
            <h1 class="sidebar-header">
                Karte des Radikal*ismus
                <span class="sidebar-close"><i class="fa fa-caret-left"></i></span>
            </h1>

            <form>
                <h2>Filter</h2>
                <fieldset>
                    <legend>Themenbereich</legend>
                    <input checked type="checkbox"><label>Anti-Rassismus</label>
                    <input checked type="checkbox"><label>Feminismus</label>
                    <input checked type="checkbox"><label>Menschenrechte</label>
                    <input checked type="checkbox"><label>Klima</label>
                </fieldset>

                <fieldset>
                    <legend>Organisationsform</legend>
                    <input checked type="checkbox"><label>NGO / Ortsgruppe</label>
                    <input type="checkbox"><label>Partei-/naher Ortsverband</label>
                </fieldset>
            </form>

        </div>

        <div class="sidebar-pane" id="profile">
            <h1 class="sidebar-header">Profile<span class="sidebar-close"><i class="fa fa-caret-left"></i></span></h1>
        </div>

        <div class="sidebar-pane" id="messages">
            <h1 class="sidebar-header">Messages<span class="sidebar-close"><i class="fa fa-caret-left"></i></span></h1>
        </div>

        <div class="sidebar-pane" id="settings">
            <h1 class="sidebar-header">Settings<span class="sidebar-close"><i class="fa fa-caret-left"></i></span></h1>
        </div>
    </div>
</div>


<style>
#mapid {
    height: 100vh;
    width: 100vw;
}
</style>

<script src="/assets/js/leaflet.js" charset="utf-8"></script>
<script src="/assets/js/easy-button.js" charset="utf-8"></script>
<script src="/assets/js/L.Control.Locate.min.js" charset="utf-8"></script>
<script src="/assets/js/leaflet-sidebar.min.js" charset="utf-8"></script>

<script>

	var mymap = L.map('mapid', {
        zoomControl: false
    }).setView([51.505, -0.09], 13);

	L.tileLayer('https://api.tiles.mapbox.com/v4/{id}/{z}/{x}/{y}.png?access_token=pk.eyJ1IjoibWFwYm94IiwiYSI6ImNpejY4NXVycTA2emYycXBndHRqcmZ3N3gifQ.rJcFIG214AriISLbB6B5aw', {
		maxZoom: 18,
		attribution: 'Map data &copy; <a href="https://www.openstreetmap.org/">OpenStreetMap</a> contributors, ' +
			'<a href="https://creativecommons.org/licenses/by-sa/2.0/">CC-BY-SA</a>, ' +
			'Imagery © <a href="https://www.mapbox.com/">Mapbox</a>',
		id: 'mapbox.streets'
	}).addTo(mymap);


    L.control.zoom({
        position: 'topright'
    }).addTo( mymap );

    var lc = L.control.locate({
        position: 'topright',
        strings: {
            title: "Show me where I am, yo!"
        }
    }).addTo( mymap );

    var sidebar = L.control.sidebar('sidebar').addTo( mymap );
    sidebar.open("filter");

    lc.start();

	L.marker([51.5, -0.09], { tags: ['fast'] }).addTo(mymap)
		.bindPopup("<b>Hello world!</b><br />I am a popup.").openPopup();

	L.circle([51.508, -0.11], 500, {
		color: 'red',
		fillColor: '#f03',
		fillOpacity: 0.5,
        tags: ['slow']
	}).addTo(mymap).bindPopup("I am a circle.");

	L.polygon([
		[51.509, -0.08],
		[51.503, -0.06],
		[51.51, -0.047]
	]).addTo(mymap).bindPopup("I am a polygon.");


	var popup = L.popup();

	function onMapClick(e) {
		popup
			.setLatLng(e.latlng)
			.setContent("You clicked the map at " + e.latlng.toString())
			.openOn(mymap);
	}

	mymap.on('click', onMapClick);


</script>
