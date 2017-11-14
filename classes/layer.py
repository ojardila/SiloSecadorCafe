class Layer:
  humidity = 0
  temperature = 0
  humidity_content_bh = 0
  bean_temperature = 0
  humidity_content_bs = 0

  def setHumidity(self,humidity):
  	self.humidity = humidity

  def setTemperature(self,temperature):
  	self.temperature = temperature

  def getNumberOfLayers(self,):
  	return len(self.layers)
  
  def setHumidityContentBh(self, hcbh):
  	self.humidity_content_bh = hcbh

  def setHumidityContentBs(self, hcbs):
  	self.humidity_content_bs = hcbs

  def setBeanTemperature(self,temperature):
  	self.bean_temperature = temperature