import csv
import re
from urllib.parse import quote
#fileout = ("BillboardTriples.txt", 'w')
with open('/Users/hu/Desktop/Index.csv', 'r') as db:
    reader = csv.DictReader(db)
    tripleList = "list of triples"
    for row in reader:
        # print(type(row['title'])):class str
        if not row['artist'] == '':
            name = ''.join(row['title'].split())
            artistUrl = quote(row['artist'], safe='')
            print ("<http://billboard.linkedmusic.org/artist/" + artistUrl + ">", "   foaf:maker",
                         "<http://billboard.linkedmusic.org/track/" + row['id'] + ">" + '.'+"\n"
                         + "<http://billboard.linkedmusic.org/track/" + row['id'] + ">", "   skos:prefLabel  ",
                         '"' + row['title'] + '"'+'.'+"\n"
                         +"<http://billboard.linkedmusic.org/artist/" + artistUrl + ">", "   skos:prefLabel  ",
                         '"' + row['artist'] + '"' +'.'+ "\n")

#fileout.close()
