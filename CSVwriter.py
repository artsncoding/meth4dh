import csv

def writeListToCSV(filename, dataList):
    with open(filename, 'w') as csvfile:
        writer = csv.writer(csvfile, delimiter=',')
        for item in dataList:
            writer.writerow([item['title'],item['publisher'],item['date']])

def writeListToCSV2(filename, dataList):
    with open(filename, 'w') as csvfile:
        writer = csv.writer(csvfile, delimiter=',')
        for item in dataList:
            writer.writerow([item['title'],item['publisher'],item['date'],item['collection']])