import csv 

filename= 'loginDetails.csv'
detailsDict = {'pythonmaster': 'changepassword', 'adminOCR': 'rsa', 'RebEl': 'ellis???!!!', 'very': 'unoriginal'} # initialise the dictionary

with open(filename, 'w', newline='') as f:
	loginDetailsWriter = csv.writer(f)
	
	for key, value in detailsDict.items(): # for every username and password in the dictionary
		loginDetailsWriter.writerow([key,value]) # writing an individual row

