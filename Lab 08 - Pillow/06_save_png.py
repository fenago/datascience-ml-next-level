# %%
'''
## How to Save Images to File
An image object can be saved by calling the save() function. This can be useful if you want
to save an image in a different format, in which case the format argument can be specified,
such as PNG, GIF, or PEG. For example, the code listing below loads the photograph in JPEG
format and saves it in PNG format.
'''

# %%
''' 
Running the example loads the JPEG image, saves it in PNG format, then loads the newly
saved image again, and confirms that the format is indeed PNG.
'''

# %%
# example of saving an image in another format
from PIL import Image
# load the image
image = Image.open('opera_house.jpg')
# save as PNG format
image.save('/tmp/opera_house.png', format='PNG')
# load the image again and inspect the format
image2 = Image.open('/tmp/opera_house.png')
print(image2.format)