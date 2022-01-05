
<img align="right" src="../images/logo.png">

Lab 9. Using PIL/Pillow
-----------------------

This lab will cover the following topics:

#### Pre-reqs:
- Google Chrome (Recommended)

#### Lab Environment
Notebooks are ready to run. All packages have been installed. There is no requirement for any setup.

Pillow is built on top of the older PIL and you can confirm that the library was installed correctly by printing the version number; for example:

```
# check PIL and Pillow version numbers
import PIL
print('Pillow Version:', PIL.__version__)
```


#### Load and Display Images

Running the example will first load the image, report the format, mode, and size, then show the image on your notebook.

```
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
```


##### Convert Images to NumPy Arrays and Back

Running the example first loads the image and then reports the data type of the array, in this case, 8-bit unsigned integers, then reports the shape of the array, in this case, 360 pixels high by 640 pixels wide and three channels for red, green, and blue. Note, the wide and height order may be listed differently (e.g. reversed), depending on your platform.

```
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
```

Running the example first loads the photo as a Pillow image then converts it to a NumPy array and reports the shape of the array. Finally, the array is converted back into a Pillow image and the details are reported.


```
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
```


#### Convert Images to NumPy Array
Both approaches are effective for loading image data into NumPy arrays, although the Matplotlib imread() function uses fewer lines of code than loading and converting a Pillow Image object and may be preferred. For example, you could easily load all images in a directory as a list as follows:

```
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
```


#### Save Images to File

Running the example loads the JPEG image, saves it in PNG format, then loads the newly saved image again, and confirms that the format is indeed PNG.

```
# example of saving an image in another format
from PIL import Image
# load the image
image = Image.open('opera_house.jpg')
# save as PNG format
image.save('/tmp/opera_house.png', format='PNG')
# load the image again and inspect the format
image2 = Image.open('/tmp/opera_house.png')
print(image2.format)
```


#### Save Images to File

Running the example loads the photograph, converts it to grayscale, saves the image in a new file, then loads it again and shows it to confirm that the photo is now grayscale instead of color.

```
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
```


#### Resize Images
Running the example first loads the photograph and reports the width and height. The image is then resized. In this case, the width is reduced to 100 pixels and the height is reduced to 56 pixels, maintaining the aspect ratio of the original image

```
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
```

#### Resize Images
Running the example loads the image, reports the shape of the image, then resizes it to have a width and height of 200 pixels.

```
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
```

#### Flip, Rotate, and Crop Images

The example below creates both horizontal and vertical flipped versions of the image.

```
# create flipped versions of an image
from PIL import Image

%matplotlib notebook
from matplotlib import pyplot
# load image
image = Image.open('opera_house.jpg')
# horizontal flip
hoz_flip = image.transpose(Image.FLIP_LEFT_RIGHT)
# vertical flip
ver_flip = image.transpose(Image.FLIP_TOP_BOTTOM)
# plot all three images using matplotlib
pyplot.subplot(311)
pyplot.imshow(image)
pyplot.subplot(312)
pyplot.imshow(hoz_flip)
pyplot.subplot(313)
pyplot.imshow(ver_flip)
pyplot.show()
```

Running the example loads the photograph and creates horizontally and vertically flipped versions of the photograph, then plots all three versions as subplots using Matplotlib. You will note that the imshow() function can plot the Image object directly without having to convert it to a NumPy array.

#### Rotate Image
The example below creates a few rotated versions of the image.

```
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
```

Running the example plots the original photograph, then a version of the photograph rotated 45 degrees, and another rotated 90 degrees. You can see that in both rotations, the pixels are clipped to the original dimensions of the image and that the empty pixels are filled with black color.


#### Cropped Image
Running the example creates a cropped square image of 100 pixels starting at 100,100 and extending down and left to 200,200. The cropped square is then displayed.

```
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
```