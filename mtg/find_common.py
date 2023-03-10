import csv
import json

# Function to convert a CSV to JSON
# Takes the file paths as arguments
# Acknowledgement: https://www.geeksforgeeks.org/convert-csv-to-json-using-python/ 

def make_json(tsv1FilePath, tsv2FilePath, jsonFilePath):
	
	# create a dictionary
	data = []
	
	# Open a csv reader called DictReader
	with open(csvFilePath, encoding='utf-8') as csvf:
		csvReader = csv.reader(csvf, delimiter="\t")
		count = 1
		
		# Convert each row into a dictionary
		# and add it to data
		for row in csvReader:
			fileDict = {}
			
			# Assuming a column named 'No' to
			# be the primary key
			fileDict["audio_id"] = count
			caption_arr = [item.lower() for item in row[1:]]
			fileDict["caption"] = ', '.join(caption_arr)
			fileDict["audio_path"] = row[0] + ".npy"
			data.append(fileDict)
			count += 1

	# Open a json writer, and use the json.dumps()
	# function to dump data
	with open(jsonFilePath, 'w', encoding='utf-8') as jsonf:
		jsonf.write(json.dumps(data, indent=3))
		
# Driver Code

# Decide the two file paths according to your
# computer system
tsv1FilePath = r'captions-timeofday.csv'
tsv2FilePath = r'captions-timeofday.csv'

tsvOutputPath = r'dataset_caption_timeofday.json'

# Call the make_json function
make_json(csvFilePath, jsonFilePath)
