import json

def trim(data):
	trimmed_dict ={}
	for key in data.keys():
	    new_key = key.replace(" ", "_")
	    if 'palatable_human' in list(data[key].keys()):
	        if data[key]['palatable_human'] == 'Yes':
	            trimmed_dict[new_key] = data[key]
	return trimmed_dict

if __name__ == "__main__":
	with open('usda.json') as datafile:
	    data = json.load(datafile)
	result = trim(data)
	with open('usda_trimmed.json', 'w') as outputfile:
		json.dump(result, outputfile)