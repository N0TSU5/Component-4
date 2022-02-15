import csv # import our module

filename = 'oddEven.csv' 

data = [ ["9","odd"] , ["2","even"] , ["131", "odd"] ] 

with open(filename, 'w', newline='') as f: # remember to open in write mode and to specify the newline parameter
	csvWriter = csv.writer(f) # create a new writer
	csvWriter.writerows(data) # writerows function allows us to write to the csv file

