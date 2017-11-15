#!/usr/bin/python2.7
# -*- coding: utf-8 -*-
from classes.dryer import Dryer
from classes.camera import Camera
from classes.layer import Layer
from classes.enviroment import Enviroment

############################################
#Dryer Properties
number_of_cameras = 2
number_of_layers = 2
delta_time = 1

#Enviroment conditions
temperature = 51.4
humidity = 16
altitude =  1250

#Initial conditions
initial_humitiy_content = 55.1
initial_bean_temperature = 22.0
height_layer = 0.13

#Output conditions conditions
time = 60.0
final_humidity_content = 11.6

#Dryer parameters
air_flow = 2098.8
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