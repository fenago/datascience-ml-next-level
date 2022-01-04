# %%
'''
## How to Load and Display Images
We need a test image to demonstrate some important features of using the Pillow library. In
this tutorial, we will use a photograph of the Sydney Opera House, taken by Ed Dunens2 and
made available on Flickr under a creative commons license, some rights reserved.

Images are typically in PNG or JPEG format and can be loaded directly using the open()
function on Image class. This returns an Image object that contains the pixel data for the
image as well as details about the image. The Image class is the main workhorse for the Pillow
library and provides a ton of properties about the image as well as functions that allow you to
manipulate the pixels and format of the image.
The format property on the image will report the image format (e.g. JPEG), the mode will
report the pixel channel format (e.g. RGB or CMYK), and the size will report the dimensions
of the image in pixels (e.g. 640 X 480). The show() function will display the image using your
operating systems default application. The example below demonstrates how to load and show
an image using the Image class in the Pillow library
'''

# %%
''' 
Running the example will first load the image, report the format, mode, and size, then show
the image on your notebook.
'''

# %%
# load and show an image with Pillow
from PIL import Image
from IPython.display import display # to display images

# load the image
image = Image.open('opera_house.jpg')
# summarize some details about the image
print(image.format)
print(image.mode)
print(image.size)
# show the image
# image.show()
display(image)