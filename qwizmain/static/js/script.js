document.addEventListener("DOMContentLoaded",function(){

 let socket = new WebSocket("ws://localhost:12345");

 socket.onopen  = () => {

 console.log("client connected!");
 socket.send("hello!");


 };

},false);





