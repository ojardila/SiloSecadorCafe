function toogleDataSeries(e){
	if (typeof(e.dataSeries.visible) === "undefined" || e.dataSeries.visible) {
		e.dataSeries.visible = false;
	} else{
		e.dataSeries.visible = true;
	}
	chart.render();
}

function graph(cameras) {
  for(camera in cameras ){

  	var data_lines = []
  	for (layer in cameras[camera]){
  		var data_object = {
		  type: "line",
		  showInLegend: true,
		  name: "Capa # "+(parseInt(layer)+1),
		  lineDashType: "dash",
		  color: "#"+((1<<24)*Math.random()|0).toString(16),
		  dataPoints: cameras[camera][layer],		
  		};
  		
  		data_lines.push(data_object);
  	}

  	var options = {
	animationEnabled: true,
	title:{
		text: "Contenido de humedad en cámara #"+(parseInt(camera))
	},
	axisX:{
		valueFormatString: "#",
		title: "Horas",
		crosshair: {
			enabled: true,
			snapToDataPoint: true
		}
	},
	axisY: {
		title: "CHBS",
		crosshair: {
			enabled: true
		}
	},
	toolTip:{
		shared:true
	},  
	legend:{
		cursor:"pointer",
		verticalAlign: "bottom",
		horizontalAlign: "left",
		dockInsidePlotArea: true,
		itemclick: toogleDataSeries
	},
	data: data_lines,
    };
    $("#chartContainer-"+camera).CanvasJSChart(options)
  }

}

