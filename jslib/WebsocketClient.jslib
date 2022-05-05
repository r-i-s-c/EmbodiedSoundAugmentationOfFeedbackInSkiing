
var WebSocketJsLib = {
	
	//InitWebSocket
	InitWebSocket: function(){
		window.wsclient = new WebSocket("ws://localhost:3000/websocket");
		console.log("Client: WebSocket initialized");
		//onopen
		window.wsclient.onopen = function(evt) { 
			console.log("Client: WebSocket opened");
			window.wsclient.send("send next");
		}; 
		//onclose
		window.wsclient.onclose = function(evt) {
			console.log("Client: WebSocket closed");
		}; 
		//onmessage
		window.wsclient.onmessage = function(evt) {
			console.log("response received");
			SendMessage("ValueInput", "UpdateValues", evt.data); //calls function in unity
			window.wsclient.send("send next");
		}; 
		//onerror
		window.wsclient.onerror = function(evt) {
			console.log("Client: WebSocket error");
		};
	},
}
mergeInto(LibraryManager.library, WebSocketJsLib);

