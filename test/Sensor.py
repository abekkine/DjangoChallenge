import time

from random import random

class Sensor(object):

    def __init__(self, location):

        self.location = location
        self.time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        self.header = "%s|%s" % (self.location, self.time)

        self.random = random


