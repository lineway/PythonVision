from PIL import Image
from numpy import *
from pylab import *

im = array(Image.open('lena.png').convert('L'))
# 图像进行反相处理
im2 = 255 - im
# 将图像像素值变换到100...200之间
im3 = (100.0/255) * im + 100
# 对图像像素求平方后得到的图像
im4 = 255.0 * (im/255.0) ** 2
image_list = [im, im2, im3, im4]
for i in image_list:
    imshow(i)
    print(int(im.min()), int(im.max()))
    show()