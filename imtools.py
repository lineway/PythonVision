import os
from PIL import Image


def get_imlist(path):
    return [os.path.join(path, f) for f in os.listdir(path) if f.endswith('.jpg')]

def translate_image_format(filelist):
    if isinstance(filelist):
        for infile in filelist:
            outfile = os.path.splitext(infile)[0] + '.jpg'
            if infile != outfile:
                try:
                    Image.open(infile).save(outfile)
                except IOError:
                    print('cannot convert', infile)

def imresize(im, sz):
    '''
    使用PIL对象重新定义图像数组的大小
    '''
    pil_im = Image.fromarray(uint8(im))
    return array(pil_im.resize(sz))

def histeq(im, nbr_bins=256):
    '''
    对一幅灰度图像进行直方图均衡化
    '''
    imhist, bins = histogram(im.flatten(), nbr_bins, normed=True)
    # cumulative distribution function
    cdf = imhist.cumsum()
    # 归一化处理
    cdf = 255 * cdf / cdf[-1]
    # 使用累积分布函数的线性插值，计算新的像素值
    im2 = interp(im.flatten(), bins[:-1], cdf)
    return im2.reshap(im.shape), cdf
