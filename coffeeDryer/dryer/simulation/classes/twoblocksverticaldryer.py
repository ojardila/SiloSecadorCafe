import math
from dryer import Dryer as Dryer
import pdb
class TwoBlocksVerticalDryer(Dryer):
  def initialize(self,):
    self.humidity_stat_layer = {}
    self.humidity_stat_average = {}

  def on(self,):
    self.initialize()
    while(self.isDrying()):
      for camera in self.cameras:
        for layer in camera.getLayers():

          if(camera.getHumidityAverage() > self.final_humidity_content):
            self.simulate(layer, camera)

          if self.cameras[0].isDone(self):
            if self.reverse:
              self.cameras[1].ReverseAirFlux()
            self.cameras[1].layers[0].setHumidity(self.enviroment.humidity/100.0)    
            self.cameras[1].layers[0].setTemperature(self.enviroment.temperature)
          else:
            self.cameras[0].layers[0].setHumidity(self.enviroment.humidity/100.0)    
            self.cameras[0].layers[0].setTemperature(self.enviroment.temperature)
          self.registerStadistic(self.clock, layer, camera)
            

        if(self.isThereFluxAirReverse()):
          if self.cameras[0].isDone(self):
            self.cameras[1].ReverseAirFlux()
            self.reverse_time = 0
          else:
            self.cameras[0].ReverseAirFlux()
          self.reverse_time = 0

      self.incrementClock()
