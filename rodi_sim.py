#!/usr/bin/env python
import web

ACTION_UNKNOWN = 0
ACTION_BLINK = 1
ACTION_SENSE = 2
ACTION_MOVE = 3
ACTION_SING = 4
ACTION_SEE = 5
ACTION_PIXEL = 6
ACTION_SENSE_LIGHT = 7
ACTION_LED = 8
ACTION_IMU = 9

urls = (
    '/1/(\d+)', 'Blink',
    '/2', 'Sense',
    '/2/', 'Sense',
    '/3/-?(\d+)/-?(\d+)', 'Move',
    '/4/(\d+)/(\d+)', 'Sing',
    '/5', 'See',
    '/5/', 'See',
    '/6/(\d+)/(\d+)/(\d+)', 'Pixel',
    '/7', 'SenseLight',
    '/7/', 'SenseLight',
    '/8/(\d+)', 'Led',
    '/9/(\d+)', 'Imu'
)


class Blink:
    def GET(self, rate):
        """ Blink LED """
        post = model.get_post(int(id))
        return render.view(post)


class Sense:
    def GET(self):
        """ Read line-follower sensors """
        return '[0, 0]'


class See:
    def GET(self):
        """ Read ultrasonic sensor"""
        print 'TODO: Return actual value'
        return '0'


class Sing:
    def GET(self, note, duration):
        """ Play a tone LED """
        print 'TODO: PlLay actual note'
        return 0


class MyApplication(web.application):
    def run(self, port=1234, *middleware):
        func = self.wsgifunc(*middleware)
        return web.httpserver.runsimple(func, ('0.0.0.0', port))

if __name__ == "__main__":
    app = MyApplication(urls, globals())
    app.run()
