# %%
'''
The Matplotlib wrapper functions can be more effective than using Pillow directly. Nevertheless, you can access the pixel data from a Pillow Image. Perhaps the simplest way is to
construct a NumPy array and pass in the Image object. The process can be reversed, converting
a given array of pixel data into a Pillow Image object using the Image.fromarray() function.
This can be useful if image data is manipulated as a NumPy array and you then want to save it
later as a PNG or JPEG file. The example below loads the photo as a Pillow Image object and
converts it to a NumPy array, then converts it back to an Image object again.
'''

# %%
''' 
Running the example first loads the photo as a Pillow image then converts it to a NumPy
array and reports the shape of the array. Finally, the array is converted back into a Pillow
image and the details are reported.
'''

# %%
# load image and convert to and from NumPy array
from PIL import Image
from numpy import asarray
# load the image
image = Image.open('opera_house.jpg')
# convert image to numpy array
data = asarray(image)
# summarize shape
print(data.shape)
# create Pillow image
image2 = Image.fromarray(data)
# summarize image details
print(image2.format)
print(image2.mode)
print(image2.size)