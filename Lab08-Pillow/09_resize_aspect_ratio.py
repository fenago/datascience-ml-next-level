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
We may not want to preserve the aspect ratio, and instead, we may want to force the pixels
into a new shape. This can be achieved using the resize() function that allows you to specify
the width and height in pixels and the image will be reduced or stretched to fit the new shape.
The example below demonstrates how to resize a new image and ignore the original aspect ratio.
'''

# %%
''' 
Running the example loads the image, reports the shape of the image, then resizes it to have
a width and height of 200 pixels.
'''

# %%
# resize image and force a new shape
from PIL import Image
from IPython.display import display # to display images

# load the image
image = Image.open('opera_house.jpg')
# report the size of the image
print(image.size)
# resize image and ignore original aspect ratio
img_resized = image.resize((200,200))
# report the size of the thumbnail
print(img_resized.size)
# show the image
# img_resized.show()
display(img_resized)

# %%
''' 
The size of the image is shown and we can see that the wide photograph has been compressed
into a square, although all of the features are still quite visible and obvious. Standard resampling
algorithms are used to invent or remove pixels when resizing, and you can specify a technique,
although default is a bicubic resampling algorithm that suits most general applications.
'''