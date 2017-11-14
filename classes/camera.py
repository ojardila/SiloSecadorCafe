class Camera:
  layers = [None] * 0
  humidity_content_average = 0
  temperature_average = 0
  
  
  def appendLayer(self, layer):
  	self.layers.append(layer)

  def setLayers(self,layers):
  	self.layers = layers

  def getNumberOfLayers(self,):
  	return len(self.layers)
  	
  def getLayers(self,):
  	return self.layers
  
  def calculateHumidityAverage(self,):
  	humidity_sum = 0.0
  	
  	for layer in self.layers:
  		humidity_sum += layer.humidity_content_bs

  	self.humidity_content_average = (humidity_sum/len(self.layers))


  def calculateTemperatureAverage(self,):
  	temperature_sum = 0.0
  	
  	for layer in self.layers:
  		temperature_sum += layer.temperature

  	self.temperature_average = (temperature_sum/len(self.layers))

  def ReverseAirFlux(self,):
  	self.layers = self.layers[::-1]