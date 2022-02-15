import csv

filename = 'loginDetails.csv'
detailsDict = {}

username = input("Enter Username ")
password = input("Enter Password ")

with open(filename, 'r') as f:
	loginDetailsReader = csv.reader(f)	
	detailsDict = dict( (rows[0], rows[1]) for rows in loginDetailsReader )

detailsDict.pop(username)
detailsDict[username] = password

with open(filename, 'w', newline='') as f:
	loginDetailsWriter = csv.writer(f)
	
	for key, value in detailsDict.items(): 
		loginDetailsWriter.writerow([key,value]) 




