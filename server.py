import tornado.ioloop
import tornado.web
from dispatcher import Dispatcher
import Settings
import uuid

class MainHandler(tornado.web.RequestHandler):
    def __init__(self):
        print ("Server Running on port %s" % self.
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
    app.listen(8888)
    tornado.ioloop.IOLoop.current().start()
