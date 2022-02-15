import csv

filename = 'loginDetails.csv'
detailsDict = {} # use curly brackets for dictionaries

with open(filename, 'r') as f:
	
	loginDetailsReader = csv.reader(f)
	
	detailsDict = dict( (rows[0], rows[1]) for rows in loginDetailsReader )
	#	the dict function allows us to write into our dictionary
	
	print(detailsDict)
