# Google Maps Route Planner
# Project 4 Python
# 01-11-2015

import urllib
import webbrowser

place = ()

def place_request():
	global route
	
	route = []
	cont = True
	count = 0
	
	print "Enter route"
	print "Press enter on black entry to route"
	
	while cont == True:
		if count ==0:
			place = raw_input("Starting Location: ")
		else:
			place = raw_input("Destination %d: " % count)	

		if place == "":
			cont = False
		else:
			route.append(place.lower().title())
			count += 1
			cont = True
						
	check_route()
	
	
	
def check_route():
	global route
	via_locs = ""
	
	if len(route) == 0:
		print "No destination entered."
		place_request()
	if len(route) == 1:
		print_request =  str(route[0])
	elif len(route) == 2:
		print_request = str(route[0]) + " to " + str(route[1]) + "."
	elif len(route) == 3:	
		print_request = str(route[0]) + " to " + str(route[2]) + " via " + str(route[1]) \
		+ "."
	elif len(route) == 4:	
		print_request = str(route[0]) + " to " + str(route[3]) + " via " + str(route[1]) \
		+ " and " + str(route[2]) + "."
	else:
		for r in range(len(route) - 4):
			via_locs +=  ", " + str(route[r + 2])
		print_request = str(route[0]) + " to " + str(route[len(route)-1]) + " via " + \
		str(route[1]) + via_locs  + " and " + str(route[(len(route)-2)]) + "."
	
	print "Generate route from " + print_request
	
	check = raw_input("Is this correct? (y/n): ")
	
	if caps(check) == Y:
		print "Redirecting to Google Maps"
		run_maps()
	else:
		place_request()
		
		
		
def run_maps():
	global route
	
	url = "https://www.google.co.uk/maps/dir/"
	
	for p in range(len(route)):
		url += route[p] + "/"
		
	print url
	
	# webbrowser.open_new(url)
	
	
def start_planner():
	print "-" * 40
	print "Welcome to Route Planner using Google Maps"
	print "-" * 40
	
	place_request()
	
start_planner()