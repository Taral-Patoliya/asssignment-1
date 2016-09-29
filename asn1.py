# NAME: 
# ST-NUMBER: 
# WORKED WITH: 

def load_asn1_data():
	"""
	This function loads the file `starbucks.csv` and returns a LIST of
	latitudes and longitudes for North American Starbucks'.
	We'll talk about lists formally in class in a few lectures, but maybe
	you can start guessing how they work based on what you see here...
	"""
	
	import csv
	
	reader = csv.reader(open('starbucks.csv', 'r'))
	locations = []
	
	for r in reader:
		locations.append( (r[0],r[1]))
		
	return locations
	
	
def convert_to_decimal(degrees,minutes,seconds):
	"""
	You fill in this one yourself!
	
	:returns: a (single) decimal lat/long
	"""
	decimal_degrees = (degrees+(minutes/60.0)+(seconds/3600.0))
	# INSERT YOUR CODE HERE!
	return decimal_degrees
	pass
	

def subtended_area(lat1,lon1,lat2,lon2):
	"""
	You fill in this one yourself!
	:returns : the area of the lat-long rectangle between the given points (in km^2)
	"""
	import math
	r = 6378.10
	area = ((math.pi/180)*(r*r)*abs(math.sin(math.radians(lat1)) - math.sin(math.radians(lat2)))*(abs(lon1 - lon2)))
	# INSERT YOUR CODE HERE!
	return area # replace this with your real return statement
	

def num_starbucks(locations,lat1,lon1,lat2,lon2):
	"""
	Function to compute the number of Starbucks in the lat-long rectangle with 
	corners lat1,lon1 and lat2,lon2. 
	
	There's new stuff in here, too. We haven't formally discussed `for` loops, so
	the loop is already done... but have a look at it. What do you think it's doing?
	
	:param locations: a list of Starbucks locations as (lat,lon) pairs
	:param lat1: Latitude for bottom left corner (in decimal degrees)
	:param lon1: Longitude for bottm left corner (in decimal degrees)
	:param lat2: Latitude for upper right corner (in decimal degrees)
	:param lon2: Longitude for upper right corner (in decimal degrees)

	:returns: An integer with the number of starbucks locations in the given rectangle
	"""
	
	# HINT: You should probably initialize some kind of 'Starbucks counter' variable here,
	# before the loop
	
	
	# This is an instruction to Python: Do the body (the indented code) following
	# `for` statement, for _every_ location in our list of locations.
	# This is a loop. It's already written for you... you just have to fill in the body
	num_starbucks = 0
	for loc in locations:
		loc_lat = float(loc[1])
		loc_lon = float(loc[0])
				
		#print loc_lat, loc_lon,  (lat1 < loc_lat), ( loc_lat < lat2), (lon1 < loc_lon), (loc_lon < lon2)
		# Okay, loc_lat now contains the latitude of the location we're considering.
		# Likewise, loc_lon contains the longitude. What _you_ have to do is:
		# - figure out if loc_lat lies between lat1 and lat2 AND loc_long lies between lon1 and lon2
		# - if that's the case, increment a variable containing the number of starbucks
		# - otherwise... do nothing at all
		
		
		# INSERT YOUR CODE HERE!
		if (lat1 < loc_lat <  lat2) and (lon1 < loc_lon < lon2):
			num_starbucks+=1

	# RETURN the value in your counter variable
	return num_starbucks
	

def starbucks_per_kmsq(lat1, lon1, lat2, lon2):
	locations = load_asn1_data()
	number =  num_starbucks(locations,lat1, lon1, lat2, lon2)
	area = subtended_area(lat1, lon1, lat2, lon2)
	density = number/area
	# INSERT YOUR CODE HERE!
	return density
	

# This line will test the density of Starbucks in the area bounded by San Diego and Boston
# Should be in the neighborhood of 0.00120 sb/km^2 (no, I don't care if you do/don't go to 100 decimal places)
print starbucks_per_kmsq(32.72,-117.16,42.35,-71.06)

