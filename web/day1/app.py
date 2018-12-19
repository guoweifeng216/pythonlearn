#!/usr/bin/env python
# coding=utf-8
"""

@athor:weifeng.guo 
@data:2018/12/19 18:49
@filename:app

"""

import tornado.ioloop
import tornado.web


class MainHandler(tornado.web.RequestHandler):
    def get(self):
        u = self.get_argument("user")
        e = self.get_argument("email")
        p = self.get_argument("pwd")
        if u == 'wfguo' and p == '123' and e == 'wfguo':
            self.write('OK')
        else:
            self.write('gun')

    def post(self, *args, **kwargs):
        u = self.get_argument("user")
        e = self.get_argument("email")
        p = self.get_argument("pwd")
        print(u, e, p)
        self.write('POST')


application = tornado.web.Application([(r"/index", MainHandler)])

if __name__ == "__main__":
    application.listen(8080)
    tornado.ioloop.IOLoop.instance().start()