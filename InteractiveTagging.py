from PIL import Image
from pylab import *


im = array(Image.open('lena.png'))
imshow(im)

print("Please click 3 points")

x = ginput(3)
print("You clicked: ", x)
show()