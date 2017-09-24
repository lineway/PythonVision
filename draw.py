from PIL import Image
from pylab import *

im = array(Image.open('lena.png'))
# 绘制原图
imshow(im)

x = [100, 100, 400, 400]
y = [200, 500, 200, 500]

# 绘制坐标点
plot(x, y, 'r*')
# 前两个坐标点连线
plot(x[:2], y[:2])

title('Plotting: "lena.png"')
show()