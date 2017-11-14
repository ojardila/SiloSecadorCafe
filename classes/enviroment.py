import math

class Enviroment:
  patm = 0
  altitude = 0
  temperature = 0
  humidity = 0

  def setAltitude(self, altitude):
  	self.altitude = altitude
    

  def setHumidity(self, humidity):
  	self.humidity = float(humidity)

  def setTemperature(self, temperature):
  	self.temperature = temperature

  def getAtmosphericPressure(self,):
  	self.patm = 9811.075 * (math.pow(10, (1.014 - float(self.altitude) / 19500)));
  	return self.patm