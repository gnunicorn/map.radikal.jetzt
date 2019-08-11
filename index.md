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
<div style="display:none">
{% for o in site.data.orgs %}
    {% assign org_id = o[0] %}
    {% assign org = o[1] %}

    {% for e in site.data[org_id] %}   
        {% capture id %}{{org_id}}-{{e[0]}}{% endcapture %}
        {% assign item=e[1] %}
        {% include popup.html item=item org=org id=id %}
    {% endfor %}
{% endfor %}
</div>
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
                    <li>
                        <label>
                            <input checked name="topic" value="diversity" type="checkbox">
                            Anti-Rassismus
                            <i class="fa fa-fist-raised" style="color:darkred"></i>
                        </label>
                    </li>
                    <li>
                        <label>
                            <input checked name="topic" value="feminism" type="checkbox">
                            Feminismus
                            <i class="fa fa-venus" style="color:purple"></i>
                        </label>
                    </li>
                    <li>
                        <label>
                            <input checked name="topic" value="humanright" type="checkbox">
                            Menschenrechte
                            <i class="fa fa-star-of-life" style="color:lightblue"></i>
                        </label>
                    </li>
                    <li>
                        <label>
                            <input checked name="topic" value="climate" type="checkbox">
                            Klima
                            <i class="fa fa-globe" style="color:lightgreen"></i>
                        </label>
                    </li>
                    </ul>
                </fieldset>
                <p></p>
                <fieldset>
                    <legend>Organisationsform</legend>
                    <ul>
                        <li>
                            <label>
                                <input checked name="org" value="ngo" type="checkbox">
                                NGO / Verein
                            </label>
                        </li>
                        <li>
                            <label>
                                <input checked name="org" value="ini" type="checkbox">
                                (freie) Initiative
                            </label>
                        </li>
                        <li>
                            <label>
                                <input type="checkbox" name="org" value="party">
                                Partei-/naher Ortsverband
                            </label>
                        </li>
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

    let I = {
        diversity: L.AwesomeMarkers.icon({
            icon: 'fist-raised',
            markerColor: 'red',
            iconColor: 'white'
        }),
        humanRights: L.AwesomeMarkers.icon({
            icon: 'star-of-life',
            markerColor: 'blue',
            iconColor: 'white'
        }),
        feminism: L.AwesomeMarkers.icon({
            icon: 'venus',
            markerColor: 'purple',
            iconColor: 'white'
        }),
        climate: L.AwesomeMarkers.icon({
            icon: 'globe',
            markerColor: 'green',
            iconColor: 'white'
        })
    };
    

	var mymap = L.map('mapid', {
        zoomControl: false
    }).setView([51.31, 13.2320], 8);

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
        onLocationError: () => {},
        strings: {
            title: "Lokalisiere mich."
        }
    }).addTo( mymap );

    var sidebar = L.control.sidebar('sidebar').addTo( mymap );
    if (window.innerWidth >= 960) {
        sidebar.open("filter");
    }

    // lc.start();

    let markers = [
        {% for o in site.data.orgs %}
            {% assign org_id = o[0] %}
            {% assign org = o[1] %}
            {% for e in site.data[org_id] %}   
                {% capture id %}{{org_id}}-{{e[0]}}{% endcapture %}
                {% assign item=e[1] %}
                {% include marker.js item=item org=org popup_id=id %},
            {% endfor %}
        {% endfor %}
        false // pending entry so we can just make a comma in the loop
    ];

    function updateMarkers() {
        let topics = [];
        let orgs = [];
        
        document.querySelectorAll("input[name=topic]").forEach(i => {
            if (i.checked) { topics.push(i.attributes.value.nodeValue) }
        });

        document.querySelectorAll("input[name=org]").forEach(i => {
            if (i.checked) { orgs.push(i.attributes.value.nodeValue) }
        });

        markers.forEach(m => {
            if (!m) return; // skip the 'false' at the end.
            var keep = false;
            if (orgs.indexOf(m.options.org) >= 0) {
                m.options.topics.forEach(t => {
                    if (topics.indexOf(t) >= 0) {
                        keep = true;
                    }
                });
            }

            if (keep) {
                m.addTo( mymap );
            } else {
                m.remove();
            }

        });
    }

    document.querySelectorAll("input[type=checkbox]")
        .forEach(e => e.addEventListener("change", updateMarkers));

    updateMarkers();

</script>
