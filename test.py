
import os, sys
import tornado.ioloop
import tornado.web

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.write('<p>%s</p>' % sys.getdefaultencoding())
        self.write('<p>%s</p>' % sys.getfilesystemencoding())

        for i in os.listdir('data'):
            #self.write(i)
            self.write('%s_' % str(len(i)))

application = tornado.web.Application([
    (r"/", MainHandler),
], debug=True)

if __name__ == "__main__":
    application.listen(8888)
    tornado.ioloop.IOLoop.instance().start()

