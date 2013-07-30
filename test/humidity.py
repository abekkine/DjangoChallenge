#!/usr/bin/python

from Sensor import Sensor

import sys

class Humidity(Sensor):

    def __init__(self, location):

        Sensor.__init__(self, location)

    def get(self):

        # Random humidity value between 20.0 and 99.0
        humidity = round(79.0 * self.random() + 20.0, 1)

        return "%s|%s%%" % (self.header, humidity)

def main():

    if len(sys.argv) < 2:
        location = 'ANKARA'
    else:
        location = sys.argv[1]

    sensor = Humidity(location)
    print sensor.get()

if __name__ == "__main__":
    main()
