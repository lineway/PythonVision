from PIL import Image
from pylab import *


im = array(Image.open('lena.png').convert('L'))

# 新建一个图像
figure()
# 不是用颜色信息
gray()
# 在原点的左上角显示轮廓图像
contour(im, origin='image')
axis('equal')
axis('off')

figure()
hist(im.flatten(), 128)

show()