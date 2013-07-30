#!/usr/bin/python

from Sensor import Sensor

import sys

class Temperature(Sensor):

    def __init__(self, location):

        Sensor.__init__(self, location)

    def get(self):

        # Random temperature value between -10.0 and 40.0
        temperature = round(50.0 * self.random() - 10.0, 1)

        return "%s|%sC" % (self.header, temperature)

def main():

    if len(sys.argv) < 2:
        location = 'ANKARA'
    else:
        location = sys.argv[1]

    sensor = Temperature(location)
    print sensor.get()

if __name__ == '__main__':
    main()
