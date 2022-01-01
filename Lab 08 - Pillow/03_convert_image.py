# %%
'''
## How to Convert Images to NumPy Arrays and Back
Often in machine learning, we want to work with images as NumPy arrays of pixel data. With
Pillow installed, you can also use the Matplotlib library to load the image and display it within
a Matplotlib frame. This can be achieved using the imread() function that loads the image as
an array of pixels directly and the imshow() function that will display an array of pixels as an
image. The example below loads and displays the same image using Matplotlib that, in turn,
will use Pillow under the covers.
'''

# %%
''' 
Running the example first loads the image and then reports the data type of the array, in
this case, 8-bit unsigned integers, then reports the shape of the array, in this case, 360 pixels
high by 640 pixels wide and three channels for red, green, and blue. Note, the wide and height
order may be listed differently (e.g. reversed), depending on your platform.
'''

# %%
# load and display an image with Matplotlib
from matplotlib import image

%matplotlib notebook
from matplotlib import pyplot
# load image as pixel array
data = image.imread('opera_house.jpg')
# summarize shape of the pixel array
print(data.dtype)
print(data.shape)
# display the array of pixels as an image
pyplot.imshow(data)
pyplot.show()