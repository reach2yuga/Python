import csv

with open('Project-2/customers-100.csv','r') as csv_file:
    csv_reader = csv.reader(csv_file)
    for i in csv_reader:
        print(i)