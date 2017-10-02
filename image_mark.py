# _*_ coding:utf-8 _*_
__author__ = 'PieLs'

'''
交互式标注，在图像中标注一些点，或者标注训练数据
'''

from PIL import Image
from pylab import *

im = array(Image.open('./lena.png'))
imshow(im)
print('Please click 3 points')
# 交互式标注
x = ginput(3)
print('you clicked: ', x)
show()
