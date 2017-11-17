class Camera:
  layers = [None] * 0
  humidity_content_average = 0
  temperature_average = 0
  number = -1
  area = 0
  
  
  def appendLayer(self, layer):
  	self.layers.append(layer)

  def setNumber(self,num):
    self.number = num
  
  def setLayers(self,layers):
  	self.layers = layers

  def setArea(self,area):
    self.area = area

  def isDone(self, dryer):
    return self.getHumidityAverage() < dryer.final_humidity_content

  def getNumberOfLayers(self,):
  	return len(self.layers)
  	
  def getLayers(self,):
  	return self.layers
  
  def getHumidityAverage(self,):
  	humidity_sum = 0.0
  	
  	for layer in self.layers:
          humidity_sum += layer.humidity_content_bs
        self.humidity_content_average = float(humidity_sum)/float(len(self.layers))
        return self.humidity_content_average


  def calculateTemperatureAverage(self,):
  	temperature_sum = 0.0
  	
  	for layer in self.layers:
  		temperature_sum += layer.temperature

  	self.temperature_average = (temperature_sum/len(self.layers))

  def ReverseAirFlux(self,):
  	self.layers = self.layers[::-1]
