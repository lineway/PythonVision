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