import csv
from SPARQLWrapper import SPARQLWrapper,JSON
from urllib.parse import quote
import time
import re
#note: please remove any " marks in the song names before put them into the query
query ="""
                      PREFIX prov: <http://www.w3.org/ns/prov#>
                      PREFIX mid: <http://purl.org/midi-ld/midi#>
                      SELECT ?filename ?pattern
                      WHERE {{ ?pattern prov:wasDerivedFrom ?filename .FILTER(regex(?filename, ".*{0}.*{1}.*$|.*{1}.*{0}.*$", "i"))}}
                                          """

#SPARQL query
with open('/Users/hu/Desktop/Index.csv', 'r') as db:
     reader = csv.DictReader(db)
     trackList=[]
     urlList=[]
     artistList=[]
     for row in reader:
         if not row['artist'] == '':
            artistUrl = quote(row['artist'], safe='')
            #urlList.append(artistUrl)
            trackName = row['title']
            artistName= row['artist']
            #print(trackName)
            sparql = SPARQLWrapper("http://virtuoso-midi.amp.ops.labs.vu.nl/sparql")
            sparql.setQuery(query.format(trackName,artistName))
            #print(query.format(trackName.strip(' ')))
            sparql.setReturnFormat(JSON)
            result = sparql.query().convert()
            pattern = re.compile(r'http\S*\'')
            text=str(result)
            m = pattern.findall(text)
            detectLength=(m.__len__())
            if not detectLength==0:
              for n in range(detectLength):
                subm=m[n]
                subm = subm.rstrip('"]')
                subm = subm.rstrip("'")
                print("<http://billboard.linkedmusic.org/track/" + row[
                  'id'] + ">")  # "<http://billboard.linkedmusic.org/artist/" + artistUrl + ">"
                print("mo:published_as")
                print("<" + subm + ">" + '.' + "\n")

            else:
               #print("<http://billboard.linkedmusic.org/track/" + row['id'] + ">" + ":no MIDI match found"+ "\n")
               pass
         time.sleep(0.5)
         # <http://billboard.linkedmusic.org/track/" + row['id'] + ">", "   mo:published_as",
