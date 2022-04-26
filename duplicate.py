from PIL import Image
from IPython.display import display
import os


path = "./pytorch-CycleGAN-and-pix2pix/results/Incremental2/test/"
path = "./pytorch-CycleGAN-and-pix2pix/results/Incremental2/test/"
dirs = os.listdir(path)


def get_concat_h(im1, im2):
    dst = Image.new('RGB', (im1.width + im2.width, im1.height))
    dst.paste(im1, (0, 0))
    dst.paste(im2, (im1.width, 0))
    return dst


def merge_image(folder):
    for filename in os.listdir(folder):
        img = Image.open(os.path.join(folder, filename)) 
        get_concat_h(img, img).save(os.path.join(folder, filename)) 
        # pixels = img.load()  # creates the pixel map
        # img.save(path+filename)


merge_image(path)
