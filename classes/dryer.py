import math
from camera import Camera as Camera
from layer import Layer as Layer
from thompson import Thompson as Thompson
import pdb

class Dryer:
  cameras = [None] * 0
  enviroment = None
  number_of_layers = 3
  number_of_cameras = 1
  initial_humitiy_content = 0
  initial_bean_temperature = 0
  height_layer = 0
  air_flow = 0
  area = 0
  time = 0
  delta_time = 1
  air_flow_reverse_time = 0
  final_humidity_content = 0
  clock = 1
  reverse_time = 1
  direction = "asc"


  def appendCamera(self, camera):
  	self.cameras.append(camera)

  def setCameras(self,cameras):
  	self.cameras = cameras

  def defineNumberCameras(self, num):
  	self.number_of_cameras = num

  def defineNumberLayersInCamera(self, num):
  	self.number_of_layers = num 
  	 	
  def getCameras(self,):
  	return self.cameras

  def getNumberOfLayers(self,):
    slay = 0
    for camera in self.cameras:
      slay += len(camera.layers)
    return slay

  def defineEnviromentProperties(self, enviroment):
  	self.enviroment = enviroment
  
  def setInitialHumidityContent(self, humidity):
    self.initial_humitiy_content = humidity

  def setInitialBeanTemperature(self, temperature):
    self.initial_bean_temperature = temperature
    
  def setHeightLayer(self, height):
    self.height_layer = height

  def setAirFlow(self,q):
    self.air_flow = q

  def setArea(self, area):
    self.area = area

  def setTime(self, time):
    self.time = time

  def setDeltaTime(self, time):
    self.delta_time = time

  def airFowReverseTime(self, time):
    self.air_flow_reverse_time = time
   
  def setFinalHumidityContent(self, humidity):
    self.final_humidity_content = float(humidity)/100

  def simulateWithThompson(self, layer):
    thompson = Thompson()
    thompson.simulate(layer, self)
  def reverseFlowAir(self,):
    self.reverse_time = 0
    for camera in self.cameras:
      camera.ReverseAirFlux()

  def setFlowDirection(self, direction):
    self.flow_direction = direction

  def getNextLayer(self, elayer):
    camera_index = 0
    for camera in self.cameras:
      layer_index = 0
      for layer in camera.layers:
        if layer == elayer:
          #If next layer is in the same camera
          if layer_index < (len(camera.layers)-1):
            if camera.layers[layer_index+1]:
              return camera.layers[layer_index+1]

          #If actual is  last layer
          if layer_index == (len(camera.layers)-1):
            if camera_index < (len(self.cameras)-1):
              next_camera = self.cameras[camera_index+1]
              if next_camera.layers[0]:
                return next_camera.layers[0]
              else:
                return None
        layer_index += 1    
      camera_index += 1

  def incrementClock(self,):
    self.clock += 1
    self.reverse_time += 1

  def getHumidityAverage(self,):
    humidity = 0.0
    for camera in self.cameras:
      camera.calculateHumidityAverage()
      humidity += camera.humidity_content_average
    return (humidity / (len(self.cameras)))


  def initialize(self, ):
    for i in range(self.number_of_cameras):
      camera = Camera()
      layers = []
      for j in range(self.number_of_layers):
        layer =  Layer()

        layer.setTemperature(self.enviroment.temperature)        
        layer.setHumidity(self.enviroment.humidity/100)
        layer.setHumidityContentBh(self.initial_humitiy_content/100)
        layer.setBeanTemperature(self.initial_bean_temperature)

        layers.append(layer)
      camera.setLayers(layers)
      self.appendCamera(camera)

      if(self.flow_direction == "desc"):
        self.reverseFlowAir()  


  def on(self,):
    self.initialize()
    while(self.getHumidityAverage() >= self.final_humidity_content or self.getHumidityAverage() == 0):

      print 'Time:' + str(self.clock)
      for camera in self.getCameras():
        print camera
        for layer in camera.getLayers():
          self.simulateWithThompson(layer)
          print str(layer.humidity_content_bs)
        camera.calculateHumidityAverage()
        print 'CHPROM Camera ' + str(camera.humidity_content_average)
        
      print 'CHPROM Dryer ' + str(self.getHumidityAverage())
      
          #Flow Direction reverse ?
      if(self.reverse_time > 0  and self.reverse_time == self.air_flow_reverse_time ):
        print 'Flux AIR Reverse'
        self.reverseFlowAir()  

      self.cameras[0].layers[0].setHumidity(self.enviroment.humidity/100)    
      self.cameras[0].layers[0].setTemperature(self.enviroment.temperature)    



      self.incrementClock()
