import csv
import re
from urllib.parse import quote
#fileout = ("BillboardTriples.txt", 'w')
with open('index.csv', 'r') as db:
    reader = csv.DictReader(db)
    tripleList = "list of triples"
    for row in reader:
        # print(type(row['title'])):class str
        if not row['artist'] == '':
            p = re.compile('"')
            findarr = p.findall(row['artist'])
            if len(findarr)== 0:
               findarr2=p.findall(row['title'])
               if len(findarr2)==0:
                   name = ''.join(row['title'].split())
                   artistUrl = quote(row['artist'], safe='')
                   print("<http://billboard.linkedmusic.org/artist/" + artistUrl + ">", "   foaf:maker",
                         "<http://billboard.linkedmusic.org/track/" + row['id'] + ">" + '.' + "\n"
                         + "<http://billboard.linkedmusic.org/track/" + row['id'] + ">", "   skos:prefLabel  ",
                         '"' + row['title'] + '"' + '.' + "\n"
                         + "<http://billboard.linkedmusic.org/artist/" + artistUrl + ">", "   skos:prefLabel  ",
                         '"' + row['artist'] + '"' + '.' + "\n")
               else:
                   name = ''.join(row['title'].split())
                   artistUrl = quote(row['artist'], safe='')
                   print("<http://billboard.linkedmusic.org/artist/" + artistUrl + ">", "   foaf:maker",
                         "<http://billboard.linkedmusic.org/track/" + row['id'] + ">" + '.' + "\n"
                         + "<http://billboard.linkedmusic.org/track/" + row['id'] + ">", "   skos:prefLabel  ",
                         '\'' + row['title'] + '\'' + '.' + "\n"
                         + "<http://billboard.linkedmusic.org/artist/" + artistUrl + ">", "   skos:prefLabel  ",
                         '"' + row['artist'] + '"' + '.' + "\n")
            else:
                if len(findarr2) == 0:
                    name = ''.join(row['title'].split())
                    artistUrl = quote(row['artist'], safe='')
                    print("<http://billboard.linkedmusic.org/artist/" + artistUrl + ">", "   foaf:maker",
                          "<http://billboard.linkedmusic.org/track/" + row['id'] + ">" + '.' + "\n"
                          + "<http://billboard.linkedmusic.org/track/" + row['id'] + ">", "   skos:prefLabel  ",
                          '"' + row['title'] + '"' + '.' + "\n"
                          + "<http://billboard.linkedmusic.org/artist/" + artistUrl + ">", "   skos:prefLabel  ",
                          '\'' + row['artist'] + '\'' + '.' + "\n")
                else:
                    name = ''.join(row['title'].split())
                    artistUrl = quote(row['artist'], safe='')
                    print("<http://billboard.linkedmusic.org/artist/" + artistUrl + ">", "   foaf:maker",
                          "<http://billboard.linkedmusic.org/track/" + row['id'] + ">" + '.' + "\n"
                          + "<http://billboard.linkedmusic.org/track/" + row['id'] + ">", "   skos:prefLabel  ",
                          '\'' + row['title'] + '\'' + '.' + "\n"
                          + "<http://billboard.linkedmusic.org/artist/" + artistUrl + ">", "   skos:prefLabel  ",
                          '\'' + row['artist'] + '\'' + '.' + "\n")
