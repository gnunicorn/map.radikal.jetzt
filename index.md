---
# Feel free to add content and custom Front Matter to this file.
# To modify the layout, see https://jekyllrb.com/docs/themes/#overriding-theme-defaults

layout: map
---

<link rel="stylesheet" href="/assets/leaflet.css" />
<link rel="stylesheet" href="/assets/leaflet.awesome-markers.css" />
<link rel="stylesheet" href="/assets/css/L.Control.Locate.min.css" />
<link rel="stylesheet" href="/assets/css/all.css" />
<link rel="stylesheet" href="/assets/css/leaflet-sidebar.min.css" />


<div id="mapid" class="sidebar-map"></div>
<div id="sidebar" class="sidebar collapsed">
    <!-- Nav tabs -->
    <div class="sidebar-tabs">
        <img src="/assets/images/favicon.png" />
        <ul role="tablist" style="padding-top: 5px">
            <li><a href="#filter" role="tab"><i class="fa fa-filter"></i></a></li>
        </ul>

        <ul role="tablist">
            <li><a href="#contribute" role="tab"><i class="fa fa-plus-circle"></i></a></li>
            <li><a href="#info" role="tab"><i class="fa fa-info-circle"></i></a></li>
        </ul>
    </div>

    <!-- Tab panes -->
    <div class="sidebar-content">
        <div class="sidebar-pane" id="filter">
            <h1 class="sidebar-header">
                Karte filtern
                <span class="sidebar-close"><i class="fa fa-times-circle"></i></span>
            </h1>

            <form>
                <p style="padding-top: 1em">zeige nur</p>
                <fieldset>
                    <legend>Themenbereiche</legend>
                    <ul>
                    <li><label><input checked type="checkbox">Anti-Rassismus <i class="fa fa-fist-raised" style="color:darkred"></i></label></li>
                    <li><label><input checked type="checkbox">Feminismus <i class="fa fa-venus" style="color:purple"></i></label></li>
                    <li><label><input checked type="checkbox">Menschenrechte <i class="fa fa-star-of-life" style="color:lightblue"></i></label></li>
                    <li><label><input checked type="checkbox">Klima <i class="fa fa-globe" style="color:lightgreen"></i></label></li>
                    </ul>
                </fieldset>
                <p></p>

                <fieldset>
                    <legend>Organisationsform</legend>
                    <ul>
                    <li><label><input checked type="checkbox">NGO / Verein</label></li>
                    <li><label><input checked type="checkbox">(freie) Initiative</label></li>
                    <li><label><input type="checkbox">Partei-/naher Ortsverband</label></li>
                    </ul>
                </fieldset>
            </form>

        </div>

        <div class="sidebar-pane" id="info">
            <h1 class="sidebar-header">Über<span class="sidebar-close"><i class="fa fa-times-circle"></i></span></h1>
        </div>

        <div class="sidebar-pane" id="contribute">
            <h1 class="sidebar-header">Contribute<span class="sidebar-close"><i class="fa fa-times-circle"></i></span></h1>
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
<script src="/assets/js/L.Control.Locate.min.js" charset="utf-8"></script>
<script src="/assets/js/leaflet.awesome-markers.min.js" charset="utf-8"></script>
<script src="/assets/js/leaflet-sidebar.min.js" charset="utf-8"></script>

<script>


    L.AwesomeMarkers.Icon.prototype.options.prefix = 'fa';

	var mymap = L.map('mapid', {
        zoomControl: false
    }).setView([51.930083, 4.507742], 13);

	L.tileLayer('https://api.tiles.mapbox.com/v4/{id}/{z}/{x}/{y}.png?access_token=pk.eyJ1IjoibWFwYm94IiwiYSI6ImNpejY4NXVycTA2emYycXBndHRqcmZ3N3gifQ.rJcFIG214AriISLbB6B5aw', {
		maxZoom: 18,
		attribution: 'Content &copy 2019 and Imprint by <a href="https://radikal.jetzt/impressum/">radikal.jetzt</a>, Map data &copy; <a href="https://www.openstreetmap.org/">OpenStreetMap</a> contributors, ' +
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

    // Add markers to map
    // Ionicons
    L.marker([51.941196, 4.512291], {
        icon: L.AwesomeMarkers.icon({
            icon: 'fist-raised',
            markerColor: 'red',
            iconColor: 'white'
        })
    }).addTo( mymap );
    L.marker([51.927913, 4.521303], {
        icon: L.AwesomeMarkers.icon({
            icon: 'star-of-life',
            markerColor: 'blue',
            iconColor: 'white'
        })
    }).addTo( mymap );
    L.marker([51.936063, 4.502077], {
        icon: L.AwesomeMarkers.icon({
            icon: 'venus',
            markerColor: 'purple',
            iconColor: 'white'
        })
    }).addTo( mymap );

    L.marker([51.932835, 4.506969], {
        icon: L.AwesomeMarkers.icon({
            icon: 'globe',
            markerColor: 'green',
            iconColor: 'white'
        })
    }).addTo( mymap );
    // L.marker([51.930295, 4.515209], {
    //     icon: L.AwesomeMarkers.icon({
    //         icon: 'heart',
    //         markerColor: 'blue'
    //     })
    // }).addTo( mymap );
    // L.marker([51.930083, 4.507742], {
    //     icon: L.AwesomeMarkers.icon({
    //         icon: 'flag',
    //         markerColor: 'blue'
    //     })
    // }).addTo( mymap );


</script>
