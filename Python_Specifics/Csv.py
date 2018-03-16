import csv

with open('example.csv') as csvfile:
    readCSV =csv.reader(csvfile,delimiter=',')
    dates=[]
    colors=[]
    for row in readCSV:
        # print(row)
        # print(row[0])
        # print(row[0],row[1])
        date=row[0]
        color=row[3]
        dates.append(date)
        colors.append(color)
    print(dates)
    print(colors)