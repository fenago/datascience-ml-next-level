# %%
'''
## How to Flip, Rotate, and Crop Images
Simple image manipulation can be used to create new versions of images that, in turn, can provide
a richer training dataset when modeling. Generally, this is referred to as data augmentation
and may involve creating flipped, rotated, cropped, or other modified versions of the original
images with the hope that the algorithm will learn to extract the same features from the image
data regardless of where they might appear. You may want to implement your own data
augmentation schemes, in which case you need to know how to perform basic manipulations of
your image data.
'''

# %%
'''
## Flip Image
An image can be flipped by calling the flip() function and passing in a method such as
FLIP LEFT RIGHT for a horizontal flip or FLIP TOP BOTTOM for a vertical flip. Other flips are
also available. The example below creates both horizontal and vertical flipped versions of the
image.
'''

# %%
# create flipped versions of an image
from PIL import Image

%matplotlib notebook
from matplotlib import pyplot
# load image
image = Image.open('opera_house.jpg')
# horizontal flip
hoz_flip = image.transpose(Image.FLIP_LEFT_RIGHT)
# vertical flip
ver_flip = image.transpose(Image.FLIP_TOP_BOTTOM)
# plot all three images using matplotlib
pyplot.subplot(311)
pyplot.imshow(image)
pyplot.subplot(312)
pyplot.imshow(hoz_flip)
pyplot.subplot(313)
pyplot.imshow(ver_flip)
pyplot.show()


# %%
'''
Running the example loads the photograph and creates horizontally and vertically flipped
versions of the photograph, then plots all three versions as subplots using Matplotlib. You will
note that the imshow() function can plot the Image object directly without having to convert
it to a NumPy array
'''