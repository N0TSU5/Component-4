import csv

filename = 'numbs.csv'

numbsDict = {}
numbsArr = []

numb1 = input()
numbLen = input()

with open(filename, 'r') as f:
	numbsReader = csv.reader(f)
	numbsDict = dict( (rows[0], rows[2]) for rows in numbsReader )

with open(filename, 'r') as f:
	numbsReader2 = csv.reader(f)
	for row in numbsReader2:
		numbsArr.append(row)

index = list(numbsDict.keys()).index(numb1)
numbsDict[numb1] = numbLen

with open(filename, 'w', newline='') as f:
	numbsWriter = csv.writer(f)
	numbsArr[index][2] = numbsDict[numb1]
	numbsWriter.writerows(numbsArr)

