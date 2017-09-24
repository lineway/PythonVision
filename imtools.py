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