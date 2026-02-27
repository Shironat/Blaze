var socket = io();

socket.on("update", function(data) {
    document.getElementById("response").innerText = data;
});