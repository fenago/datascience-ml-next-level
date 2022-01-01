# %%
'''
## Cropped Image
An image can be cropped: that is, a piece can be cut out to create a new image, using the crop()
function. The crop function takes a tuple argument that defines the two x and y coordinates of
the box to crop out of the image. For example, if the image is 2,000 by 2,000 pixels, we can clip
out a 100 by 100 pixel box in the image. The example below demonstrates how to create a new
image as a crop from a loaded image.
'''

# %%
'''
Running the example creates a cropped square image of 100 pixels starting at 100,100 and
extending down and left to 200,200. The cropped square is then displayed.
'''

# %%
# example of cropping an image
from PIL import Image
from IPython.display import display # to display images

# load image
image = Image.open('opera_house.jpg')
# create a cropped image
cropped = image.crop((100, 100, 200, 200))
# show cropped image
# cropped.show()
display(cropped)
