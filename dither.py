from PIL import Image
import numpy as np
import math


# the dither images are 8*8 pixels in dimension. 
# only change this if you change the size of the dither image

ditherDim = 8;


# save the image in the "input" folder, and change the name below:

startImageName = "mandelbrot.png"




# determines what level of grey a pixel falls on, ranging 0-4.

def posterize(pix):
    return math.floor((pix / 255) * 5)


#each dither image is opened and turned into a numpy array to make the processing easier.

with Image.open("ditherGradient/g0.png") as im:
    grey = im.convert('L')
    dither0 = np.array(grey)

with Image.open("ditherGradient/g1.png") as im:
    grey = im.convert('L')
    dither1 = np.array(grey)

with Image.open("ditherGradient/g2.png") as im:
    grey = im.convert('L')
    dither2 = np.array(grey)

with Image.open("ditherGradient/g3.png") as im:
    grey = im.convert('L')
    dither3 = np.array(grey)

with Image.open("ditherGradient/g4.png") as im:
    grey = im.convert('L')
    dither4 = np.array(grey)


# open the starting image
# convert it to greyscale
# convert the greyscaled image to a numpy array
# iterate through the array and map the corresponding dither to the numpy array

with Image.open(f"input/{startImageName}") as im:

    width = im.width
    height = im.height
    grey = im.convert('L')
    im_array = np.array(grey)

    for y in range(height):
        for x in range(width):
            if posterize(im_array[y][x]) == 0:
                im_array[y][x] = dither0[y % ditherDim] [x % ditherDim]
            elif posterize(im_array[y][x]) == 1:
                im_array[y][x] = dither1[y % ditherDim] [x % ditherDim]
            elif posterize(im_array[y][x]) == 2:
                im_array[y][x] = dither2[y % ditherDim] [x % ditherDim]
            elif posterize(im_array[y][x]) == 3:
                im_array[y][x] = dither3[y % ditherDim] [x % ditherDim]
            elif posterize(im_array[y][x]) >= 4:
                im_array[y][x] = dither4[y % ditherDim] [x % ditherDim]
                         

# convert the numpy array to an image and save it

newImg = Image.fromarray(im_array, 'L')
newImg.save(f'output/processed{startImageName}')

newImg.show()
    