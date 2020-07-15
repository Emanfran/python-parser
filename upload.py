import re

textReader = open("wordList.txt","r")
output = open("result.txt", "a")

if textReader.mode =="r":
    content = textReader.read()

type1 = content.split('\n')

print("starting....")

for  x in range(len(type1)):
    output.write('"'+type1[x]+'"')

print("Done....")






