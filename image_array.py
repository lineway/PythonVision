# _*_ coding:utf-8 _*_
__author__ = 'PieLs'

from PIL import Image
from pylab import *

im = array(Image.open('./lena.png'))
print(im.shape, im.dtype)
