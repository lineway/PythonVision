# _*_ coding:utf-8 _*_
__author__ = 'PieLs'

from PIL import Image
from pylab import *

# 读取图像到数组中
im = array(Image.open('./lena.png'))

# 绘制图像
imshow(im)

# 定义一些点
x = [100, 100, 400, 400]
y = [200, 500, 200, 500]

# 使用红色，星状标记绘制点
plot(x, y, 'r*')

# 绘制连接前两个点的线
plot(x[:2], y[:2], 'ks:')

# 添加标题，显示绘制的图像
title('Plotting: "empire.jpg"')

# 定义是否显示坐标轴
axis('off')

show()
