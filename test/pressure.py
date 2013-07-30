#!/usr/bin/python

from Sensor import Sensor

import sys

class Pressure(Sensor):

    def __init__(self, location):

        Sensor.__init__(self, location)

    def get(self):

        # Random pressure value between 750.0 and 770.0
        pressure = round(20.0 * self.random() + 750.0, 1)

        return "%s|%smmHg" % (self.header, pressure)

def main():

    if len(sys.argv) < 2:
        location = 'ANKARA'
    else:
        location = sys.argv[1]

    sensor = Pressure(location)
    print sensor.get()

if __name__ == "__main__":
    main()
