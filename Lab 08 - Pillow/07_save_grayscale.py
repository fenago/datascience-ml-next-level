# %%
'''
## How to Save Images to File
Saving images is useful if you perform some data preparation on the image before modeling.
One example is converting color images (RGB channels) to grayscale (1 channel). There are a
number of ways to convert an image to grayscale, but Pillow provides the convert() function
and the mode ‘L’ will convert an image to grayscale.
'''

# %%
''' 
Running the example loads the photograph, converts it to grayscale, saves the image in a
new file, then loads it again and shows it to confirm that the photo is now grayscale instead of
color.
'''

# %%
# example of saving a grayscale version of a loaded image
from PIL import Image
from IPython.display import display # to display images

# load the image
image = Image.open('opera_house.jpg')
# convert the image to grayscale
gs_image = image.convert(mode='L')
# save in jpeg format
gs_image.save('/tmp/opera_house_grayscale.jpg')
# load the image again and show it
image2 = Image.open('/tmp/opera_house_grayscale.jpg')
# show the image
# image2.show()
display(image2)