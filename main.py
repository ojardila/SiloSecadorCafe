#!/usr/bin/python2.7
# -*- coding: utf-8 -*-
from classes.dryer import Dryer
from classes.camera import Camera
from classes.layer import Layer
from classes.enviroment import Enviroment

############################################
#Dryer Properties
number_of_cameras = 1
number_of_layers = 3
delta_time = 1

#Enviroment conditions
temperature = 40.1
humidity = 26
altitude =  1250

#Initial conditions
initial_humitiy_content = 40.2
initial_bean_temperature = 21
height_layer = 0.4

#Output conditions conditions
time = 60
final_humidity_content = 12

#Dryer parameters
air_flow = 456
area = 1

flow_direction =  "asc" #can be desc

#Flow reverse conditions
air_flow_reverse_time = 6

############################################


if __name__ == '__main__':

  enviroment = Enviroment()
  enviroment.setAltitude(altitude)
  enviroment.setTemperature(temperature)
  enviroment.setHumidity(humidity)

  dryer = Dryer()
  dryer.defineEnviromentProperties(enviroment)
  dryer.defineNumberCameras(number_of_cameras)
  dryer.defineNumberLayersInCamera(number_of_layers)

  dryer.setInitialHumidityContent(initial_humitiy_content)
  dryer.setInitialBeanTemperature(initial_bean_temperature)
  dryer.setHeightLayer(height_layer)

  dryer.setAirFlow(air_flow)
  dryer.setFlowDirection(flow_direction)
  
  dryer.setArea(area)

  dryer.setTime(time)
  dryer.setDeltaTime(delta_time)

  dryer.airFowReverseTime(air_flow_reverse_time)
  dryer.setFinalHumidityContent(final_humidity_content)



  dryer.on()