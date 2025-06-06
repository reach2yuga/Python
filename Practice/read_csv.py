import csv

with open('/workspaces/Python/CSVFileHandling/names.csv', 'r') as read_csv:
    csv_reader = csv.reader(read_csv)
    for line in csv_reader:
     print(line)