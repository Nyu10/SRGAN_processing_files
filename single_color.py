import numpy as np
import matplotlib.pyplot as plt
from skimage.io import imshow, imread
from skimage.color import rgb2hsv, hsv2rgb
import cv2
from PIL import Image
from IPython.display import display
import os


# path0 = "./dataset/colored/red/single/test/"
path0 = "./dataset/single_color/"
dirs = os.listdir(path0)


def load_images_from_folder(folder):
    for i in range(0,3):
        colors = ["blue", "green", "red"]
        path1 = "./dataset/triple_color_tests/"+colors[i]+"/test/"
        count = 0
        for filename in os.listdir(folder):
            src = cv2.imread(os.path.join(folder, filename), cv2.IMREAD_UNCHANGED)
            red_channel = src[:,:,i]
            src[:,:,((i+2) %3)] = np.zeros(red_channel.shape)
            src[:,:,((i+1) % 3)] = np.zeros(red_channel.shape)
            src[:,:,i] = red_channel
            cv2.imwrite(os.path.join(path1,filename), src)
            count+=1
            if (count%100 == 0):
                print(colors[i] + " "+str(count))
        print("finished ", colors[i])
images = load_images_from_folder(path0)