import os
import re
dirRoot='/Users/hu/Desktop/McGill-Billboard'
k=open("timestampTriples.txt",'a',encoding='utf-8')
for parent,dirnames, filenames in os.walk(dirRoot):
     for filepath in filenames:
         txtPath = os.path.join(parent, filepath)
         if ".DS_Store" in txtPath:
               pass
         else:
            #k.write(txtPath.strip('/Users/hu/Desktop/McGill-Billboard').rstrip('/salami_chords.txt') +'\n')
            trackurl = ("<http://billboard.linkedmusic.org/track/" + txtPath.strip(
                '/Users/hu/Desktop/McGill-Billboard').rstrip('/salami_chords.txt') + '>'+'\n')
            segmenturl = ("<http://billboard.linkedmusic.org/segmentLine/" + txtPath.strip(
                '/Users/hu/Desktop/McGill-Billboard').rstrip('/salami_chords.txt') + '> ')
            id = (txtPath.strip('/Users/hu/Desktop/McGill-Billboard').rstrip('/salami_chords.txt'))
            line1 = (trackurl + "meld:segment " + segmenturl+" ." +'\n')
            line2 = (segmenturl + "a so:SegmentLine ."+'\n')
            mainpart=line1+line2
            k.write(mainpart)
            content = open(txtPath, encoding='utf-8')
            text=content.read()
            list=text.split()
            endPoint=len(list)
            keywords=["main-theme,","secondary-theme,", "intro,","applause,","talking,","verse,","interlude,","coda,","refrain,","pre-chorus,","chorus,","bridge,","instrumental,","trans,","transition,", "outro,","solo,","end","silence"]
            count=-1
            i=0
            timeStampCollector = []
            newSt=''
            for p in range(endPoint):
                word = list[p]
                if not word in keywords:
                    pass
                else:
                    count=count+1
            #indexing the total num of segments
            for p in range(endPoint):
                 word=list[p]
                 if not word in keywords:
                      pass
                 else:
                      if word == "silence":
                          timeStamp = list[p - 1]
                          newSt = float(timeStamp)
                          timeStampCollector.append(str(newSt))
                      elif word == "end":
                          timeStamp = list[p - 1]
                          newSt = float(timeStamp)
                          timeStampCollector.append(str(newSt))
                      else:
                          word=word.rstrip(',')
                          timeStamp = list[p - 2]
                          #print(p, list)
                          newSt = float(timeStamp)
                          timeStampCollector.append(str(newSt))
                          #print(i, trackurl)
            #print(timeStampCollector)
            for p in range(endPoint):
                 #output = str(word + ":" + str(timeStamp))
                 word = list[p]
                 segmentLabel = str(word).rstrip(',')
                 subSegmentLine = (segmenturl.strip('> .') + "/" + str(i) + '>')
                 if not word in keywords:
                      pass
                 else:
                     if word == "silence":
                         timeStamp = list[p - 1]
                         newSt = float(timeStamp)
                     elif word == "end":
                         timeStamp = list[p - 1]
                         newSt = float(timeStamp)
                     else:
                         word = word.rstrip(',')
                         timeStamp = list[p - 2]
                         # print(p, list)
                         newSt = float(timeStamp)
                     if i == 0:
                             line3 = (subSegmentLine + ' a so:Segment ;' + '\n')
                             line4 = ("   rdfs:label" + ' "' + segmentLabel + '" ;'+ '\n')
                             line5 = ("   tl:beginsAtDuration " + '"PT' + str(newSt) + 'S"^^xsd:duration' + ' ;' + '\n')
                             line6 = ("   tl:endsAtDuration " + '"PT' + timeStampCollector[i + 1] + 'S"^^xsd:duration' + ' ;' + '\n')
                             line7 = ("   so:segmentAfter " + segmenturl.strip('> .') + "/" + str(i + 1) + '>'+ ';'+'\n')
                             line8 = ("   so:onSegmentLine"+"  "+ segmenturl+' .')
                             combo1=line3+line4+line5+line6+line7+line8
                             k.write(combo1)

                     else:
                           if i == count:
                                 line3 = (subSegmentLine + ' a so:Segment ;' + '\n')
                                 line4 = ("   rdfs:label" + ' "' + segmentLabel + '" ;'+ '\n')
                                 line5 = ("   tl:beginsAtDuration " + '"PT' + str(newSt) + 'S"^^xsd:duration' + ' ;' + '\n')
                                 line6 = ("   so:segmentBefore " + segmenturl.strip('> .') + "/" + str(i - 1) + '>'+ ';'+ '\n')
                                 line7 = ("   so:onSegmentLine" + '"PT' + segmenturl+' .')
                                 combo2 = line3 + line4 + line5 + line6 + line7
                                 k.write(combo2)
                           else:
                                 line3 = (subSegmentLine + ' a so:Segment ;' + '\n')
                                 line4 = ("   rdfs:label" + ' "' + segmentLabel + '" ;'+ '\n')
                                 line5 = ("   tl:beginsAtDuration " + '"PT' + str(newSt) + 'S"^^xsd:duration' + ' ;' +'\n')
                                 line6 = ("   tl:endsAtDuration " + '"PT' + timeStampCollector[i+1] + 'S"^^xsd:duration'+ ' ;'+'\n')
                                 line7 = ("   so:segmentAfter " + segmenturl.strip('> .') + "/" + str(i + 1) + '>' + ';' + '\n')
                                 line8 = ("   so:segmentBefore " + segmenturl.strip('> .') + "/" + str(i - 1) + '>' + ';' + '\n')
                                 line9 = ("   so:onSegmentLine" + "  " + segmenturl+' .')
                                 combo3 = line3 + line4 + line5 + line6 + line7+line8+line9
                                 k.write(combo3)
                     i = i + 1
                     k.write('\n')