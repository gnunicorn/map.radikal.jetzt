{% assign item=include.item %}L.marker([{{item.location[0]}}, {{item.location[1]}}], {
    icon: I.{{item.topics[0]}},
    org: "{{item.org}}",
    topics: ["{{item.topics | join:'","' }}"]
}).bindPopup(document.getElementById('{{include.popup_id}}'))