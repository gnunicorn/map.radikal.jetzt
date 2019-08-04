{% assign item=include.item %}
{% assign org=include.org %}

L.marker([{{item.location.lat}}, {{item.location.lng}}], {
    icon: I.{{item.topics[0]|default:org.topics[0]}},
    org: "{{item.org|default:org.type}}",
    topics: ["{{item.topics| default: org.topics | join:'","' }}"]
}).bindPopup(document.getElementById('{{include.popup_id}}'))