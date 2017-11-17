jQuery(document).ready(function(){
	$('#same-data-dryer').change(function() {
		if($(this).is(":checked")) {
			jQuery("#area-cam2").val(jQuery("#area-cam1").val());
			jQuery("#cont-hum-cam2").val(jQuery("#cont-hum-cam1").val());
			jQuery("#temperature-cam2").val(jQuery("#temperature-cam1").val());
		} else {
			jQuery("#area-cam2").val("");
			jQuery("#cont-hum-cam2").val("");
			jQuery("#temperature-cam2").val("");       
		}

	});

	$('#reverse-flux').change(function() {
	if($(this).is(":checked")) {
		jQuery(".period-reversing-container").show();
		jQuery("#reverse-time").val('');

	} else {
		jQuery(".period-reversing-container").hide();

		jQuery("#reverse-time").val('0');
	}

	});
});