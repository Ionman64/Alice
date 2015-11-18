import tornado.ioloop
import tornado.web
from dispatcher import Dispatcher
from settings import Settings
import uuid

settings = Settings()

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        dispatch = Dispatcher(str(uuid.uuid4()))
        self.write(dispatch.getIdentifier())
        print (self.get_argument("q"))
        

def make_app():
    return tornado.web.Application([
        (r"/", MainHandler),
    ])

if __name__ == "__main__":
    app = make_app()
    app.listen(settings.getSetting("portNum"))
    tornado.ioloop.IOLoop.current().start()
