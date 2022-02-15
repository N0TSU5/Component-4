import csv

filename = 'loginDetails.csv'

loginData = []
singleUserData = []

username = None # declaring the variables
password = None

with open(filename, 'w', newline='') as f:
	loginDetailsWriter = csv.writer(f) # create a new writer with the file parameter
	
	while(True):
		
		username = input("\nEnter new username")
		if(username == "END"):
			break # ends the loop
		
		password = input("\nEnter new password")
		
		singleUserData.append(username) # appending to our row
		singleUserData.append(password)
		
		loginData.append(singleUserData) # appending the row to our 2d array
		singleUserData = [] # empty the 1D array
		
		###print("\n",loginData)
		
	loginDetailsWriter.writerows(loginData) # write the 2d array to our file once user finished
	

