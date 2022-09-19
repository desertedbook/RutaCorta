
let map = L.map('map').setView([23.634501,-102.552784],5)

//Agregar tilelAyer mapa base desde openstreetmap
L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png',{
    maxZoom:18,
}).addTo(map);

var n = 16.84942;
var m = -99.90891;

//L.marker([n,m]).addTo(map);
//L.marker([18.51413,-88.30381]).addTo(map);

var polygon = L.polygon([
    [16.84942,-99.90891],
    [18.51413,-88.30381],
    [18.51413,-88.30381]
]).addTo(map);


