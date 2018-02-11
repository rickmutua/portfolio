$('.smooth').on('click', function() {
    $.smoothScroll({
        scrollElement: $('body'),
        scrollTarget: '#' + this.id
    });

    return false;
});

var http = require("http");
setInterval(function() {
    http.get("http://erick-mutua.herokuapp.com");
}, 300000); // every 5 minutes (300000)