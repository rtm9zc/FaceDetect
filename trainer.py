from os import listdir
from random import choice, randrange
from window import Window, FaceWindow
import skimage, skimage.io, skimage.transform

CONST_NUMTOUSE = 100 #number of faces analyzed for training set
CONST_IMAGEDIR = 'images/'
CONST_FACELISTFILE = 'facelist.txt'
CONST_TRAININGFACES = 'trainingset/face/'
CONST_TRAININGOTHER = 'trainingset/notface/'


def extractSquare(image, row, col, size):
    return image[row:row+size, col:col+size]

imageList = listdir(CONST_IMAGEDIR)
imageDict = {} #mapping image -> bool, true if it has a face in it
for i in imageList: #initialize dict to all falses
    imageDict[i] = False
faceList = []
with open(CONST_FACELISTFILE, 'r') as f:
    for line in f.readlines():
        currentFace = FaceWindow(line)
        faceList.append(currentFace)
        imageDict[currentFace.fileName] = True
facelessImages = []
for key in imageDict:
    if not imageDict[key]:
        facelessImages.append(key)

for i in range(0, CONST_NUMTOUSE):
    #output a face reduced to 12x12
    currentFace = choice(faceList)
    faceList.remove(currentFace)
    faceImage = skimage.img_as_float(skimage.io.imread(CONST_IMAGEDIR 
                                                     + currentFace.fileName))
    squaredFaceWindow = Window(currentFace, faceImage.shape)
    squaredImage = extractSquare(faceImage, squaredFaceWindow.rowMin, 
                                 squaredFaceWindow.colMin, 
                                 squaredFaceWindow.width)
    outFaceImage = skimage.transform.resize(squaredImage, (12, 12))
    skimage.io.imsave(CONST_TRAININGFACES + 'image' + str(i) + '.jpg', outFaceImage)
    #output a random 12x12 patch from something with no faces
    currentImage = choice(facelessImages)
    theImage = skimage.img_as_float(skimage.io.imread(CONST_IMAGEDIR 
                                                    + currentImage))
    row = randrange(0, theImage.shape[0] - 12)
    col = randrange(0, theImage.shape[1] - 12)
    outNotFace = extractSquare(theImage, row, col, 12)
    skimage.io.imsave(CONST_TRAININGOTHER + 'image' + str(i) + '.jpg', outNotFace)
