import json
from CSVwriter import writeListToCSV, writeListToCSV2
from yearExtractor import extractYears

with open('fng-data-dc.json', encoding="utf8") as json_data:
    d = json.load(json_data)


data = {}
data['artWork'] =  []

data2 = {}
data2['artWork'] = []


for item in d['descriptionSet']:
    item_title='no title'
    item_publisher='no publisher'
    a_date = 'no date'
    collection = 'no collection'

    if('title' in item):
        for title in item['title']:
            if('fi' in title):
                item_title = title['fi']

    if('publisher' in item):
        for pub in item['publisher']:
            if('unit' in pub):
                item_publisher = pub['unit']

    if('date' in item):
        for date in item['date']:
            if('acquisition' in date):
                a_date = extractYears(date['acquisition'])
                data['artWork'].append({
                    'title': item_title,
                    'publisher': item_publisher,
                    'date': a_date
                })

    if('relation' in item):
        for relation in item['relation']:
            if('collection' in relation):
                collection = relation['collection']
                data2['artWork'].append({
                    'title':item_title,
                    'publisher': item_publisher,
                    'date': a_date,
                    'collection': collection
                })


writeListToCSV('dateData.csv', data['artWork'])
writeListToCSV2('collectionData.csv', data2['artWork'])
         




