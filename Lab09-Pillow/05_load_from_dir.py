# %%
''' 
## How to Convert Images to NumPy Array
Both approaches are effective for loading image data into NumPy arrays, although the
Matplotlib imread() function uses fewer lines of code than loading and converting a Pillow
Image object and may be preferred. For example, you could easily load all images in a directory
as a list as follows:
'''

# %%
# load all images in a directory
from os import listdir
from matplotlib import image
# load all images in a directory
loaded_images = list()
for filename in listdir('images'):
	# load image
	img_data = image.imread('images/' + filename)
	# store loaded image
	loaded_images.append(img_data)
	print('> loaded %s %s' % (filename, img_data.shape))