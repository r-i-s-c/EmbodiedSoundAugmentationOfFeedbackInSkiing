from pkgutil import ImpImporter
from tornado.options import options, define
import tornado.httpserver
import tornado.ioloop
import tornado.web
import tornado.wsgi
import tornado.websocket
import json
from Sensoren import sensor1, sensor2, sensor3

define('port', type=int, default=3000)

class HelloHandler(tornado.web.RequestHandler):
    def get(self):
        self.render("index.html")

class clientJS(tornado.web.RequestHandler):
    def get(self):
        f = open("WebsocketClient.jslib","r")
        self.write(f.read())
        f.close()

class MyWebSocket(tornado.websocket.WebSocketHandler):
    
    def check_origin(self, origin):
        return True
    
    def open(self):
        print("Server: WebSocket opened")

    def on_message(self, message):
        print("request: " + message)
        values = {
            "s1RotX": sensor1.getRotData()["xAxis"],
            "s1RotY": sensor1.getRotData()["yAxis"],
            "s2RotX": sensor2.getRotData()["xAxis"],
            "s2RotY": sensor2.getRotData()["yAxis"],
            "s3RotX": sensor3.getRotData()["xAxis"],
            "s3RotY": sensor3.getRotData()["yAxis"],
        }
        json_str = json.dumps(values) #convert to json string
        self.write_message(json_str) # message to client

    def on_close(self):
        print("Server: WebSocket closed")

def main():
    tornado_app = tornado.web.Application([
        ('/', HelloHandler),
        ('/websocket', MyWebSocket),
        ('/WebsocketClient.jslib', clientJS),
        ])
    server = tornado.httpserver.HTTPServer(tornado_app)
    server.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()

if __name__ == '__main__':
    main()
