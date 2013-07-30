from Sensor import Sensor

class Temperature(Sensor):

    def __init__(self, location):

        Sensor.__init__(self, location)
        self.temperature = 0.0

    def get(self):

        self.temperature = self.temperature + 0.5

        return "%s|%s|%s" % (self.location, self.time, self.temperature)
