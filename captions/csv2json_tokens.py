import csv
import json

# Function to convert a CSV to JSON
# Takes the file paths as arguments
# Acknowledgement: https://www.geeksforgeeks.org/convert-csv-to-json-using-python/ 

def make_json(csvFilePath, jsonFilePath):
	
	# create a dictionary
	data = []
	
	# Open a csv reader called DictReader
	with open(csvFilePath, encoding='utf-8') as csvf:
		csvReader = csv.reader(csvf)
		
		# Convert each row into a dictionary
		# and add it to data
		for row in csvReader:
			fileDict = {}
			
			# Assuming a column named 'No' to
			# be the primary key
			fileDict["track_id"] = row[0]
			caption_arr = [item.lower() for item in row[1:]]
			raw_caption = ', '.join(caption_arr)
			caption = {
				"raw": raw_caption,
				"tokens": ' '.join(caption_arr).split(' ')
         }
			fileDict["caption"] = caption
			data.append(fileDict)

	# Open a json writer, and use the json.dumps()
	# function to dump data
	with open(jsonFilePath, 'w', encoding='utf-8') as jsonf:
		jsonf.write(json.dumps(data, indent=3))
		
# Driver Code

# Decide the two file paths according to your
# computer system
csvFilePath = r'captions.csv'
jsonFilePath = r'dataset_tokens.json'

# Call the make_json function
make_json(csvFilePath, jsonFilePath)
