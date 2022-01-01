# %%
'''
## How to Resize Images
It is important to be able to resize images before modeling. Sometimes it is desirable to
thumbnail all images to have the same width or height. This can be achieved with Pillow using
the thumbnail() function. The function takes a tuple with the height and width, and the image
will be resized so that the height and width of the image are equal or smaller than the specified
shape.
For example, the test photograph we have been working with has the width and height of
(640, 360). We can resize it to (100, 100), in which case the largest dimension, in this case, the
width, will be reduced to 100, and the height will be scaled in order to retain the aspect ratio of
the image. The example below will load the photograph and create a smaller thumbnail with a
width and height of 100 pixels.
'''

# %%
''' 
Running the example first loads the photograph and reports the width and height. The
image is then resized. In this case, the width is reduced to 100 pixels and the height is reduced
to 56 pixels, maintaining the aspect ratio of the original image
'''

# %%
# create a thumbnail of an image
from PIL import Image
from IPython.display import display # to display images

# load the image
image = Image.open('opera_house.jpg')
# report the size of the image
print(image.size)
# create a thumbnail and preserve aspect ratio
image.thumbnail((100,100))
# report the size of the modified image
print(image.size)
# show the image
# image.show()
display(image)