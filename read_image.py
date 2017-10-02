# _*_ coding:utf-8 _*_
__author__ = 'PieLs'

from PIL import Image
from pylab import *

pil_im = Image.open('./lena.png')
# 创建图像的缩略图
# new_pil = pil_im.thumbnail((128, 128))

# 复制和粘贴图像区域
# box = (100, 100, 400, 400)
# region = pil_im.crop(box)
# region = region.transpose(Image.ROTATE_180)
# pil_im.paste(region, box)

# 调整图像大小, 大小为元组数据
# out = pil_im.resize((128, 128))

# 旋转图像，角度为逆时针方向
out = pil_im.rotate(45)

out.show()
