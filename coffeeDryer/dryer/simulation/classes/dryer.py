import math
from camera import Camera as Camera
from layer import Layer as Layer
from thompson import Thompson as Thompson
import pdb

class Dryer:
  cameras = [None] * 0
  enviroment = None
  number_of_layers = 1
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
  humidity_stat_layer = {}
  humidity_stat_average = {}


  temperature_stat_layer = {}
  direction = "asc"


  def appendCamera(self, camera):
  	self.cameras.append(camera)

  def setCameras(self,cameras):
  	self.cameras = cameras

  def getNumberofCamera(self, ecamera):
    index = 0 
    for camera in self.cameras:
      if camera == ecamera:
        return index
      index += 1

  def defineNumberCameras(self, num):
  	self.number_of_cameras = num

  def getHumidityStat():
    return self.humidity_stat_layer

  def defineNumberLayersInCamera(self, num):
  	self.number_of_layers = num 
  	 	
  def setCameras(self,cameras):
    self.cameras=cameras
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
    self.initial_humitiy_content = float(humidity)

  def setInitialBeanTemperature(self, temperature):
    self.initial_bean_temperature = float(temperature)
    
  def setHeightLayer(self, height):
    self.height_layer = float(height)

  def setAirFlow(self,q):
    self.air_flow = float(q)

  def setArea(self, area):
    self.area = float(area)

  def setTime(self, time):
    self.time = float(time)

  def isThereFluxAirReverse(self,):
    return (self.reverse_time > 0  and self.reverse_time == self.air_flow_reverse_time )

  def setDeltaTime(self, time):
    self.delta_time = float(time)

  def registerStadistic(self, time, elayer, camera):
    if not(self.clock in self.humidity_stat_layer):
      self.humidity_stat_layer[time] = {}

    if not(self.clock in self.humidity_stat_average):
      self.humidity_stat_average[time] = {}
    


    if not( camera.number in self.humidity_stat_layer[time]):
      self.humidity_stat_layer[time][camera.number] = {}
    self.humidity_stat_layer[(time)][camera.number][elayer.level]=elayer.humidity_content_bs
    self.humidity_stat_average[time][camera.number] = camera.getHumidityAverage()
    if time> 1:
      if(self.humidity_stat_average[(time-1)][camera.number] == 0 or self.humidity_stat_average[(time-1)][camera.number] == self.humidity_stat_average[(time)][camera.number]):
        self.humidity_stat_layer[(time)][camera.number][elayer.level]=0
        self.humidity_stat_average[time][camera.number] = 0
    


  def airFowReverseTime(self, time):
    self.air_flow_reverse_time = time
   
  def setFinalHumidityContent(self, humidity):
    self.final_humidity_content = float(humidity)/100.0

  def simulate(self, layer, camera):
    thompson = Thompson()
    thompson.simulate(layer, self, camera)

  def reverseFlowAir(self,):
    self.reverse_time = 0
    if(len(self.cameras) > 0):
      self.cameras[0].ReverseAirFlux()
    #self.cameras = self.cameras[::-1]


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

  def isDrying(self,):
    flag = True
    for camera in self.cameras:
      camera.getHumidityAverage()
      if camera.getHumidityAverage() < self.final_humidity_content:
        flag = False
      else:
        flag = True
    if len(self.cameras) == 0:
       return False
    return flag



  def initialize(self, ):
    print 'i'

  #   for i in range(self.number_of_cameras):
  #     camera = Camera()
  #     layers = []
  #     for j in range(self.number_of_layers):
  #       layer =  Layer()

  #       layer.setTemperature(self.enviroment.temperature)        
  #       layer.setHumidity(self.enviroment.humidity/100)
  #       layer.setHumidityContentBh(self.initial_humitiy_content/100)
  #       layer.setBeanTemperature(self.initial_bean_temperature)

  #       layers.append(layer)
  #     camera.setLayers(layers)
  #     self.appendCamera(camera)

  #     if(self.flow_direction == "desc"):
  #       self.reverseFlowAir()  


  def on(self,):
    stop = False
    while(self.isDrying() or self.isDrying() == 0 and stop==False):
      print '========================'
      print 'Time:' + str(self.clock)
      for camera in self.getCameras():
        print camera
        for layer in camera.getLayers():
          self.simulateWithThompson(layer)
          print str(layer.humidity_content_bs)
        camera.calculateHumidityAverage()
        print 'CHPROM Camera ' + str(camera.humidity_content_average)
        if camera.humidity_content_average < self.final_humidity_content:
          self.reverse_time = 0
          self.reverseFlowAir()
          print ''' TERMINA CAMARA SECADO '''

        print '=='
      print 'CHPROM Dryer ' + str(self.getHumidityAverage())
      
          #Flow Direction reverse ?
      if(self.reverse_time > 0  and self.reverse_time == self.air_flow_reverse_time ):
        print 'Flux AIR Reverse'
        self.reverseFlowAir()
      if(len(self.cameras) == 0):
        stop=True
      else:
        self.cameras[0].layers[0].setHumidity(self.enviroment.humidity/100)    
        self.cameras[0].layers[0].setTemperature(self.enviroment.temperature)    



      self.incrementClock()
