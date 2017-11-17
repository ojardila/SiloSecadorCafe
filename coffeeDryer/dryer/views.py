# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from simulation.classes.twoblocksverticaldryer import TwoBlocksVerticalDryer
from simulation.classes.camera import Camera
from simulation.classes.layer import Layer
from simulation.classes.enviroment import Enviroment

import pdb




def index(request):
    context = {}
    template = loader.get_template('dryer/index.html')
    return HttpResponse(template.render(context, request))


def simulate(request):
    context = {}
    initial_humitiy_content_cam1 = float()
    initial_humitiy_content_cam2 = float()
    area_cam1=float()
    area_cam2=float()
    initial_bean_temperature_cam1=float()
    initial_bean_temperature_cam2=float()
    temperature=float()
    humidity=float()
    altitude=float()
    height_layer=float()
    air_flow=float()
    final_humidity_content=float()
    reverse_time=float()
    reverse_flux=False
    num_layers=float()
    
    if 'cont-hum-cam1' in request.GET:
      initial_humitiy_content_cam1 = float(request.GET['cont-hum-cam1'])

    if 'cont-hum-cam2' in request.GET:
      initial_humitiy_content_cam2 = float(request.GET['cont-hum-cam2'])

    if 'area-cam1' in request.GET:
      area_cam1 = float(request.GET['area-cam1'])

    if 'area-cam2' in request.GET:
      area_cam2 = float(request.GET['area-cam2'])

    if 'temperature-cam1' in request.GET:
      initial_bean_temperature_cam1 = float(request.GET['temperature-cam1'])

    if 'temperature-cam2' in request.GET:
      initial_bean_temperature_cam2 = float(request.GET['temperature-cam2'])

    if 'temperature' in request.GET:
      temperature = float(request.GET['temperature'])

    if 'humidity' in request.GET:
      humidity = float(request.GET['humidity'])

    if 'altitude' in request.GET:
      altitude = float(request.GET['altitude'])

    if 'height' in request.GET:
      height_layer = float(request.GET['height'])

    if 'flux' in request.GET:
      air_flow = float(request.GET['flux'])

    if 'chfbs' in request.GET:
      final_humidity_content = float(request.GET['chfbs'])

    if 'reverse-flux' in request.GET:
      reverse_flux = float(request.GET['reverse-flux'])

    if 'reverse-time' in request.GET:
      reverse_time = float(request.GET['reverse-time'])

    if 'layers' in request.GET:
      num_layers = int(request.GET['layers'])      


    #Enviroment conditions
    enviroment = Enviroment()
    enviroment.setAltitude(altitude)
    enviroment.setTemperature(temperature)
    enviroment.setHumidity(humidity)

    dryer = TwoBlocksVerticalDryer()
    dryer.defineEnviromentProperties(enviroment)
    dryer.defineNumberCameras(2)
    dryer.defineNumberLayersInCamera(num_layers)
    dryer.setInitialHumidityContent(initial_humitiy_content_cam1)
    dryer.setInitialBeanTemperature(initial_bean_temperature_cam1)
    dryer.setHeightLayer(height_layer)


    dryer.setAirFlow(air_flow)
    dryer.setFlowDirection("asc")  
    dryer.setArea(area_cam1)

    if reverse_flux:
      dryer.enableReverseFlux(reverse_flux)
      dryer.airFowReverseTime(reverse_time)
    dryer.setFinalHumidityContent(final_humidity_content)

    #Camera 1
    camera1 = Camera()
    layers = []
    for i in range(num_layers):
      layer =  Layer()
      layer.setLevel(i)
      layer.setTemperature(enviroment.temperature)        
      layer.setHumidity(enviroment.humidity/100.0)
      layer.setHumidityContentBh(initial_humitiy_content_cam1/100.0)
      layer.setBeanTemperature(initial_bean_temperature_cam1)
      layers.append(layer)
      camera1.setNumber(1)
      camera1.setArea(area_cam1)
      camera1.setLayers(layers)
    #Agregar area

    #Camera 2
    camera2 = Camera()
    layers = []
    for j in range(num_layers):
      layer =  Layer()
      layer.setLevel(j)
      layer.setTemperature(enviroment.temperature)        
      layer.setHumidity(enviroment.humidity/100.0)
      layer.setHumidityContentBh(initial_humitiy_content_cam2/100.0)
      layer.setBeanTemperature(initial_bean_temperature_cam2)
      layers.append(layer)
    camera2.setNumber(2)
    camera2.setArea(area_cam2)
    camera2.setLayers(layers)
    #   #Agregar area

    dryer.setCameras([camera1,camera2])

    dryer.on()

    context['humidity_table'] = dryer.humidity_stat_layer
    context['dryer'] = dryer
    context['num_cameras'] = range(dryer.number_of_cameras)
    context['colspan_layers'] = num_layers+1


    template = loader.get_template('dryer/simulate.html')

    return HttpResponse(template.render(context, request))
