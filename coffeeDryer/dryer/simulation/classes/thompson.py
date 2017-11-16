import math
import pdb
class Thompson:
  def simulate(self, layer, dryer, camera):
    iteration = True
    saturation = False
    while iteration:
      if saturation:
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
      capacity = cmsg * float(dryer.height_layer) * float(dryer.area)

      # Simulation
      #Bean air relation
      r = vesp * capacity / (dryer.getNumberOfLayers() * dryer.air_flow * dryer.delta_time)
      specifi_cheat = (1.3556 + (5.7859 * chbs)) * 0.2385 * r;
      equilibrium_temperature = ((0.24 + 0.45 * hc) * layer.temperature + layer.bean_temperature * specifi_cheat) / (0.24 + 0.45 * hc + specifi_cheat)
      equilibrium_humidity = 0.01 * (61.030848 * layer.humidity - 108.37141 * (math.pow(layer.humidity, 2)) + 74.461059 * (math.pow(layer.humidity, 3))) * math.exp((-0.037049 * layer.humidity + 0.070114 * (math.pow(layer.humidity, 2)) - 0.035177 * (math.pow(layer.humidity, 3))) * (layer.temperature + 0))
      deft = pvs * (1 - layer.humidity) / 1000
      dmdt = -0.0143 * 1.06439 * (chbs - equilibrium_humidity) * (math.pow(deft, 0.87898)) * (math.pow(float(dryer.clock), (1.06439 - 1)))

      humidity_content_bs_final = chbs + dmdt * dryer.delta_time
      humidity_content_new = humidity_content_bs_final / (1 + humidity_content_bs_final)
      deltah = (chbs - humidity_content_bs_final) * r
      hf = hc + deltah;
      clv = (2502.4 - 2.42958 * float(layer.bean_temperature)) * (1 + 1.44408 * math.exp(-21.5011 * chbs)) * 0.239
      tn = ((0.24 + 0.45 * hc) * equilibrium_temperature - deltah * (587.9 + clv - equilibrium_temperature) + specifi_cheat * equilibrium_temperature) / (0.24 + 0.45 * hf + specifi_cheat)      
      final_pvs = math.exp(60.433 - (6834.271 / (tn + 273.16)) - (5.16923 * math.log((tn + 273.16))))
      new_relative_humidity = dryer.enviroment.getAtmosphericPressure() * hf / (final_pvs * (hf + 0.622));
      new_temperature = tn

      if new_relative_humidity < 1:
        iteration = False
        saturation = False

      if  new_relative_humidity > 1:
        iteration = True
        saturation = True


    layer.setTemperature(tn);
    layer.setHumidity(new_relative_humidity);
    layer.setBeanTemperature(new_temperature);
    layer.setHumidityContentBs(humidity_content_bs_final);
    layer.setHumidityContentBh(humidity_content_new);
    



    if(dryer.getNextLayer(layer) is not None):
      dryer.getNextLayer(layer).setTemperature(tn);
      dryer.getNextLayer(layer).setHumidity(new_relative_humidity);

