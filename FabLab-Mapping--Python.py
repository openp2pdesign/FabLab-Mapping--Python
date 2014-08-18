# -*- coding: utf-8 -*-
# <nbformat>3.0</nbformat>

# <headingcell level=1>

# Mapping the world of FabLabs

# <markdowncell>

# Prerequisites (on MacOSX):
# 
# * brew install geos
# * brew install gdal
# * brew install gfortran
# 
# * pip install matplotlib
# * pip install requests
# * pip install basemap --allow-external basemap

# <headingcell level=2>

# Load the data from fablabs.io API

# <codecell>

from mpl_toolkits.basemap import Basemap
import json
import requests
from pprint import pprint

# <codecell>

# Load FabLab list
url = "https://api.fablabs.io/v0/labs.json"
fablab_list = requests.get(url).json()

# Print a beautified version of the FabLab list
# print json.dumps(fablab_list, sort_keys=True, indent=4)

features = {}
features["type"] = "FeatureCollection"
features_list = []

for k,i in enumerate(fablab_list["labs"]):
	# print "Name:", i["name"]
	# print "Latitude:", i["latitude"]
	# print "Logitude:", i["longitude"]
	# print "Link:",i["url"]	
	# print
	feature_dict = {}
	coord = []
	coord.append(i["longitude"])
	coord.append(i["latitude"])
	feature_dict["type"] = "Feature"
	feature_dict["properties"] = {}
	feature_dict["geometry"] = {}
	feature_dict["properties"]["name"] = i["name"]
	feature_dict["properties"]["link"] = i["url"]
	feature_dict["geometry"]["type"] = "Point"
	feature_dict["geometry"]["coordinates"] = coord
	if i["latitude"] and i["longitude"] != "null": 
		features_list.append(feature_dict)

features["features"] = features_list

# print "Our GEOjson:"
# print json.dumps(features, sort_keys=True, indent=4)

with open('data.json', 'w') as outfile:
	json.dump(features, outfile)

# <codecell>

# Load the data
json_data=open("data.json")
data = json.load(json_data)

# Check the data
# pprint(data)

# Read data
x = []
y = []

for i in data["features"]:
    x.append(i["geometry"]["coordinates"][0])
    y.append(i["geometry"]["coordinates"][1])

# <headingcell level=2>

# Europe

# <codecell>

figure(figsize=(15,15))

# create the map: Europe
id_map = Basemap()
id_map = Basemap(llcrnrlon=-30, llcrnrlat=25, # lower left corner
                 urcrnrlon=40, urcrnrlat=80, # upper right corner
                 resolution="h") 

# draw important features
id_map.drawcoastlines(linewidth=.3) 
id_map.drawcountries(linewidth=.2)
id_map.fillcontinents(color='0.8') # Light gray
id_map.drawmapboundary()

# Transform from (lat, lon) to (x, y) 
x1, y1 = id_map(x, y)

# Plot data
for i in xrange(len(x1)):
    id_map.plot(x1[i], y1[i], 'or', 
                markersize=7, 
                alpha=.5)
    
# Save the file
plt.savefig('FabLabs-Europe.pdf')

# <headingcell level=2>

# Asia

# <codecell>

figure(figsize=(15,15))

# create the map: Asia
id_map = Basemap()
id_map = Basemap(llcrnrlon=30, llcrnrlat=-40, # lower left corner
                 urcrnrlon=155, urcrnrlat=80, # upper right corner 
                 resolution = "h") 

# draw important features
id_map.drawcoastlines(linewidth=.3) 
id_map.drawcountries(linewidth=.2)
id_map.fillcontinents(color='0.8') # Light gray
id_map.drawmapboundary()

# Transform from (lat, lon) to (x, y) 
x1, y1 = id_map(x, y)

# Plot data
for i in xrange(len(x1)):
    id_map.plot(x1[i], y1[i], 'or', 
                markersize=10, 
                alpha=.5)

# Save the file
plt.savefig('FabLabs-Asia.pdf')

# <headingcell level=2>

# Africa

# <codecell>

figure(figsize=(15,15))

# create the map: Africa
id_map = Basemap()
id_map = Basemap(llcrnrlon=-30, llcrnrlat=-40, # lower left corner
                 urcrnrlon=55, urcrnrlat=40, # upper right corner 
                 resolution = "h") 

# draw important features
id_map.drawcoastlines(linewidth=.3) 
id_map.drawcountries(linewidth=.2)
id_map.fillcontinents(color='0.8') # Light gray
id_map.drawmapboundary()

# Transform from (lat, lon) to (x, y) 
x1, y1 = id_map(x, y)

# Plot data
for i in xrange(len(x1)):
    id_map.plot(x1[i], y1[i], 'or', 
                markersize=10, 
                alpha=.5)

# Save the file
plt.savefig('FabLabs-Africa.pdf')

# <headingcell level=2>

# America

# <codecell>

figure(figsize=(15,15))

# create the map: America
id_map = Basemap()
id_map = Basemap(llcrnrlon=-180, llcrnrlat=-70, # lower left corner
                 urcrnrlon=-30, urcrnrlat=90, # upper right corner 
                 resolution = "h") 

# draw important features
id_map.drawcoastlines(linewidth=.3) 
id_map.drawcountries(linewidth=.2)
id_map.fillcontinents(color='0.8') # Light gray
id_map.drawmapboundary()

# Transform from (lat, lon) to (x, y) 
x1, y1 = id_map(x, y)

# Plot data
for i in xrange(len(x1)):
    id_map.plot(x1[i], y1[i], 'or', 
                markersize=10, 
                alpha=.5)

# Save the file
plt.savefig('FabLabs-America.pdf')

# <codecell>


