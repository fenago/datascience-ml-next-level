# %%
'''
## How to Install Pillow
The Python Imaging Library, or PIL for short, is an open source library for loading and
manipulating images. It was developed and made available more than 25 years ago and has
become a de facto standard API for working with images in Python. The library is now defunct
and no longer updated and does not support Python 3. Pillow is a PIL library that supports
Python 3 and is the preferred modern library for image manipulation in Python. It is even
required for simple image loading and saving in other Python scientific libraries such as SciPy
and Matplotlib.

The Pillow library is installed as a part of most SciPy installations; for example, if you are
using Anaconda. If you manage the installation of Python software packages yourself for your
workstation, you can easily install Pillow using pip; for example:

sudo pip install Pillow

Pillow is built on top of the older PIL and you can confirm that the library was installed
correctly by printing the version number; for example:
'''


# %%
# check PIL and Pillow version numbers
import PIL
print('Pillow Version:', PIL.__version__)
