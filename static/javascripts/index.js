window.onload = function(){
	var manfSelect = document.getElementById("id_manufacturer");
	var carSelect = document.getElementById("id_car");
	
	sendManf();

	function sendManf(){
		var strManf = manfSelect.options[manfSelect.selectedIndex].text;

		var url = "/ajax_api/"+strManf;
		var xmlhttp = new XMLHttpRequest();
		xmlhttp.open('GET', url, true);
		xmlhttp.onreadystatechange = function() {
			if (xmlhttp.readyState == 4) {
				if(xmlhttp.status == 200) {
					//Deleting previous options
					(function(sel) {
						while(sel.options.length > 0){                
							sel.remove(0);
						}
					})(carSelect);

					var arr = JSON.parse(xmlhttp.responseText);
					//Inserting new options
					for(var i = 0; i < arr.length; i++){
						var car = arr[i]["name"];
						var option = document.createElement("option");
						option.value = i+1;
						option.text = car;
						carSelect.add(option);
					}
				}
			}
		};
		xmlhttp.send();

	}
	
	manfSelect.onchange = function() {
		sendManf();
	};
};
