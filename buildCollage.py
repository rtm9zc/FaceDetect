import skimage, skimage.io
from skimage.transform import rescale
from numpy import zeros

CONST_OUTWIDTH = 480
CONST_OUTHEIGHT = 240
CONST_FACEDIR = 'trainingset/face/'
CONST_OTHERDIR = 'trainingset/notface/'

def copyIn(outImage, inImage, rowStart, colStart):
    for row in range(0, 24):
        for col in range(0, 24):
            outImage[row+rowStart][col+colStart] = inImage[row][col]

outImage = zeros((CONST_OUTHEIGHT, CONST_OUTWIDTH))
for row in range(0, CONST_OUTHEIGHT, 24):
    for col in range(0, CONST_OUTWIDTH, 24):
        if (col < CONST_OUTWIDTH/2): #face images
            index = (row/24)*(CONST_OUTWIDTH/2)/24 + col/24
            print('FACE ', index)
            imageLoc = CONST_FACEDIR + 'image' + str(index) + '.jpg'
            theImage = skimage.img_as_float(skimage.io.imread(imageLoc))
            theImage = rescale(theImage, 2, mode='nearest')
            copyIn(outImage, theImage, row, col)
        else: #not faces
            index = (row/24)*(CONST_OUTWIDTH/2)/24 + (col-(CONST_OUTWIDTH/2))/24
            print('OTHER ', index)
            imageLoc = CONST_OTHERDIR + 'image' + str(index) + '.jpg'
            theImage = skimage.img_as_float(skimage.io.imread(imageLoc))
            theImage = rescale(theImage, 2, mode='nearest')
            copyIn(outImage, theImage, row, col)
skimage.io.imsave('collage.jpg', outImage)
