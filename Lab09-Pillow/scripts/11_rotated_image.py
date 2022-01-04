# %%
'''
## Rotate Image
An image can be rotated using the rotate() function and passing in the angle for the rotation.
The function offers additional control such as whether or not to expand the dimensions of the
image to fit the rotated pixel values (default is to clip to the same size), where to center the
rotation of the image (default is the center), and the fill color for pixels outside of the image
(default is black). The example below creates a few rotated versions of the image.
'''

# %%
# create rotated versions of an image
from PIL import Image

%matplotlib notebook
from matplotlib import pyplot
# load image
image = Image.open('opera_house.jpg')
# plot original image
pyplot.subplot(311)
pyplot.imshow(image)
# rotate 45 degrees
pyplot.subplot(312)
pyplot.imshow(image.rotate(45))
# rotate 90 degrees
pyplot.subplot(313)
pyplot.imshow(image.rotate(90))
pyplot.show()


# %%
'''
Running the example plots the original photograph, then a version of the photograph rotated
45 degrees, and another rotated 90 degrees. You can see that in both rotations, the pixels are
clipped to the original dimensions of the image and that the empty pixels are filled with black
color.
'''