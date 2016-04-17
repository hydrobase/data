import json
from pymongo import MongoClient

# fill in the DB URI and client from the config.py in the app repo
client = MongoClient('XXXXXX')
db = client['XXXX']

with open('usda_trimmed.json') as datafile:
	    data = json.load(datafile)

for key in data.keys():
	# to see which key and data is being pushed to MongoDB
	print(data[key])
	print("\n")
	db.plant_profiles.insert_one(data[key])