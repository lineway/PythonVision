from PIL import Image
from pylab import *

im = array(Image.open('lena.png'))
print(im.shape, im.dtype)

im = array(Image.open('lena.png').convert('L'), 'f')
print(im.shape, im.dtype)

print(im[10].mean())