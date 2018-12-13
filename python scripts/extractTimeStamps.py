import os
import re
dirRoot='/Users/hu/Desktop/McGill-Billboard'
k=open("StructualInfor.txt",'a',encoding='utf-8')
for parent,dirnames, filenames in os.walk(dirRoot):
     for filepath in filenames:
         txtPath = os.path.join(parent, filepath)
         if ".DS_Store" in txtPath:
               pass
         else:
            k.write(txtPath.strip('/Users/hu/Desktop/McGill-Billboard') + 't'+'\n')
            content = open(txtPath, encoding='utf-8')
            text=content.read()
            #k.write(text)
            list=text.split()
            endPoint=len(list)
            #print(endPoint)
            #print(list)
            keywords=["fade in,", "intro,","verse,","interlude,","coda,","pre-chorus,","chorus,","bridge,","instrumental,","trans,","outro,","solo,","fadeout","end","silence"]
            for p in range(endPoint):
                word=list[p]
                #print(word)
                if not word in keywords:
                     pass
                else:
                     if word == "fadeout,":
                         timeStamp = list[p - 1]
                     elif word == "silence":
                         timeStamp = list[p - 1]
                     elif word == "end":
                         timeStamp = list[p - 1]
                     else:
                         word=word.rstrip(',')
                         timeStamp = list[p - 2]
                     output =str(word + ":" + timeStamp)
                     #print(output)
                     k.write(output+'\n')
     k.write('\n')
 #k.close()
