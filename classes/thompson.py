import math
import pdb
class Thompson:
  def simulate(self, layer, dryer):
    bandera = True
    bandera2 = False
    while bandera:
      if bandera2:
        layer.bean_temperature = layer.bean_temperature + 0.1

      #Air Calculations
      pvs = math.exp(60.433 - (6834.271 / (layer.temperature + 273.16)) - (5.16923 * math.log((layer.temperature + 273.16))))
      pv = pvs * layer.humidity
      hc = 0.6219 * pv / (dryer.enviroment.getAtmosphericPressure() - pv)
      vesp = (287 * (layer.temperature + 273.16)) / (dryer.enviroment.getAtmosphericPressure() - pv)

      #bean calculations
      chbs = layer.humidity_content_bh / (1 - layer.humidity_content_bh)
      pesp = 365.884 + (2.7067 * 100 * chbs)
      cmsg = pesp * (1 - layer.humidity_content_bh  )
      capacidad = cmsg * float(dryer.height_layer) * float(dryer.area)

      # Simulation
      #Bean air relation
      r = vesp * capacidad / (dryer.getNumberOfLayers() * dryer.air_flow * dryer.delta_time)
      calorespecifico = (1.3556 + (5.7859 * chbs)) * 0.2385 * r;
      tEquilibrio = ((0.24 + 0.45 * hc) * layer.temperature + layer.bean_temperature * calorespecifico) / (0.24 + 0.45 * hc + calorespecifico)
      hEquilibrio = 0.01 * (61.030848 * layer.humidity - 108.37141 * (math.pow(layer.humidity, 2)) + 74.461059 * (math.pow(layer.humidity, 3))) * math.exp((-0.037049 * layer.humidity + 0.070114 * (math.pow(layer.humidity, 2)) - 0.035177 * (math.pow(layer.humidity, 3))) * (layer.temperature + 0))
      deficit = pvs * (1 - layer.humidity) / 1000
      dmdt = -0.0143 * 1.06439 * (chbs - hEquilibrio) * (math.pow(deficit, 0.87898)) * (math.pow(float(dryer.clock), (1.06439 - 1)))

      chbsf = chbs + dmdt * dryer.delta_time
      chNew = chbsf / (1 + chbsf)
      deltaH = (chbs - chbsf) * r
      hf = hc + deltaH;
      clv = (2502.4 - 2.42958 * float(layer.bean_temperature)) * (1 + 1.44408 * math.exp(-21.5011 * chbs)) * 0.239
      tNew = ((0.24 + 0.45 * hc) * tEquilibrio - deltaH * (587.9 + clv - tEquilibrio) + calorespecifico * tEquilibrio) / (0.24 + 0.45 * hf + calorespecifico)      
      pvsFinal = math.exp(60.433 - (6834.271 / (tNew + 273.16)) - (5.16923 * math.log((tNew + 273.16))))
      hrNew = dryer.enviroment.getAtmosphericPressure() * hf / (pvsFinal * (hf + 0.622));
      tgNew = tNew

      if hrNew < 1:
        bandera = False
        bandera2 = False

      if  hrNew > 1:
        bandera = True
        bandera2 = True


    layer.setTemperature(tNew);
    layer.setHumidity(hrNew);
    layer.setBeanTemperature(tgNew);
    layer.setHumidityContentBs(chbsf);
    layer.setHumidityContentBh(chNew);
    



#    pdb.set_trace()
    if(dryer.getNextLayer(layer) is not None):
      dryer.getNextLayer(layer).setTemperature(tNew);
      dryer.getNextLayer(layer).setHumidity(hrNew);

