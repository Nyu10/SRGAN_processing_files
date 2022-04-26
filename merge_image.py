from PIL import Image
from IPython.display import display
import os


# path = "./pytorch-CycleGAN-and-pix2pix/results/colored/all/1488"
# path_blue = path + "/blue.png"
# path_green = path + "/green.png"
# path_red = path + "/red.png"
# path_combined = path + "/combined2.png"

path = "./pytorch-CycleGAN-and-pix2pix/results/colored/all/679"
path_blue = path + "/blue.png"
path_green = path + "/green.png"
path_red = path + "/red.png"
path_combined = path + "/combined2.png"
dirs = os.listdir(path)


def merge_image(folder):

        img_blue = Image.open(path_blue)
        pixels_blue = img_blue.load()
        img_red = Image.open(path_red)
        pixels_red = img_red.load()
        img_green = Image.open(path_green)
        pixels_green = img_green.load()
        for i in range(0, 256):
            for j in range(0, 256):
                # new_arr = [0,0,0]
                # for k in range(0, 3):
                #     new_arr[k] = pixels_blue[i,j][k] + pixels_red[i, j][k] + pixels_green[i, j][k]        
                # pixels_blue[i, j] = tuple(new_arr)
                pixels_blue[i, j] = ( pixels_red[i, j][0] , pixels_green[i, j][1], pixels_blue[i,j][2])
               
                # for k in range(0,3):
                #     pixels_blue[i, j][k] = pixels_blue[i,j][k] + pixels_red[i, j][k] + pixels_green[i, j][k]        

        img_blue.save(path_combined)


merge_image(path)
