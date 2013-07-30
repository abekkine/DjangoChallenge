import time

class Sensor(object):

    def __init__(self, location):

        self.location = location
        self.time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())

