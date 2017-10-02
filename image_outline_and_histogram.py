# _*_ coding:utf-8 _*_
__author__ = 'PieLs'
'''
图像轮廓和直方图
'''

from PIL import Image
from pylab import *

# 读取图像到数组中
im = array(Image.open('./lena.png').convert('L'))

# 新建一个图像
figure()
# 不使用颜色信息
gray()
# 在原点的左上角显示轮廓图像
contour(im, origin='image')
axis('equal')
axis('off')

figure()
# 直方图中接受以为数组作为参数，第二个参数是划分区域的数量，直方图中纵坐标显示的是落在该区域中像素点的数量
hist(im.flatten(), 128)
show()
