from os import listdir
from window import Window, FaceWindow

imageList = listdir('images/')
imageDict = {} #mapping image -> bool, true if it has a face in it
for i in imageList: #initialize dict to all falses
    imageDict[i] = False
with open('facelist.txt', 'r') as f:
    for line in f.readlines():
        
    
