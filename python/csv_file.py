import csv

with open('./csv_file.csv', mode='r') as file:
    csvFile=csv.reader(file, delimiter=',')
    for idx, lines in enumerate(csvFile):
        if idx==0:
            print("Header:", " ".join(lines))
        else:
            print("Row", idx, ":", ", ".join(lines))