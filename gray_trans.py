from PIL import Image
from numpy import *
from pylab import *

im = array(Image.open('./lena.png').convert('L'))

im2 = 255 - im
im3 = (100.0/255) * im + 100
im4 = 255.0 * (im/255.0) ** 2

print(int(im.min()), int(im.max()))

imshow(im2)
show()
imshow(im3)
show()
imshow(im4)
show()
