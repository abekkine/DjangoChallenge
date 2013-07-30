#!/usr/bin/python

from Sensor import Sensor

import sys

class Wind(Sensor):

    def __init__(self, location):

        Sensor.__init__(self, location)

    def get(self):

        # Random speed value between 0.0 and 100.0
        speed = round(100.0 * self.random(), 1)
        # Random direction value between 0 and 360
        direction = int(360 * self.random())

        return "%s|%sknts|%sdeg" % (self.header, speed, direction)

def main():

    if len(sys.argv) < 2:
        location = 'ANKARA'
    else:
        location = sys.argv[1]

    sensor = Wind(location)
    print sensor.get()

if __name__ == "__main__":
    main()

