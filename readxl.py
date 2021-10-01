import csv

# open file for reading
with open('exp1.csv', 'r', newline='', encoding='latin-1') as csvDataFile:

    # read file as csv file
    csvReader = csv.reader(csvDataFile)

    # for every row, print the row
    for row in csvReader:
        print(row)
