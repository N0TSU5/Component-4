import csv

filename = 'loginDetails.csv'

with open(filename, 'r'):
	loginDetailsReader = csv.reader(f)
	
	for row in loginDetailsReader:
		print("\nUsername:",row[0]) # row[0] is the first cell of the row
		print("Password:",row[1]) # row[1] is the second cell; the password
