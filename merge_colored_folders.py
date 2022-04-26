# import the necessary packages
from typing import final
from skimage.metrics import structural_similarity as ssim
import matplotlib.pyplot as plt
import numpy as np
import cv2
import os
from PIL import Image, ImageChops
import os
from MSE_SSIM import mse

origin_path = "./pytorch-CycleGAN-and-pix2pix/results/colored/colored/test_latest/images/"
save_path = "./pytorch-CycleGAN-and-pix2pix/results/MSE_combined/"
red_path = "./pytorch-CycleGAN-and-pix2pix/results/MSE/red/MSEred/test_latest/images/"
green_path = "./pytorch-CycleGAN-and-pix2pix/results/MSE/green/MSEgreen/test_latest/images/"
blue_path = "./pytorch-CycleGAN-and-pix2pix/results/MSE/blue/MSEblue/test_latest/images/"

def merge_image(red,blue,green, num):
    pixels_red = red.load()
    pixels_blue = blue.load()
    pixels_green = green.load()
    for i in range(0, 256):
        for j in range(0, 256):
            pixels_blue[i, j] = ( pixels_red[i, j][0] , pixels_green[i, j][1], pixels_blue[i,j][2])
               
    final_path = save_path + "_"+str(num)+"_combined.png"
    blue.save(final_path)
    return final_path

#writes differences to file
f = open(save_path+"analysis.txt", "w")
mse_sum=0
ssim_sum=0
num_images=0
nums = [10,13,138,679,1488,4938,5008,6799,7246,7271,9992,9998]
for num in nums:
    red_img_path = os.path.join(red_path, str(num)+ "_fake_B.png")
    blue_img_path = os.path.join(blue_path, str(num)+ "_fake_B.png")
    green_img_path = os.path.join(green_path, str(num)+ "_fake_B.png")
    origin = cv2.imread(os.path.join(origin_path, str(num)+ "_real_B.png"), cv2.IMREAD_GRAYSCALE)
    red = Image.open(red_img_path)
    green = Image.open(green_img_path)
    blue = Image.open(blue_img_path)
    generated = cv2.imread(os.path.join(merge_image(red,blue,green, num)),cv2.IMREAD_GRAYSCALE)
    
    # red = cv2.imread(os.path.join(red_path, str(num) + "_fake_B.png"),cv2.IMREAD_GRAYSCALE)
    # green = cv2.imread(os.path.join(green_path, str(num) + "_fake_B.png"),cv2.IMREAD_GRAYSCALE)
    # blue = cv2.imread(os.path.join(blue_path, str(num) + "_fake_B.png"),cv2.IMREAD_GRAYSCALE)
    # original = cv2.cvtColor(original, cv2.COLOR_BGR2GRAY)
    # generated = cv2.cvtColor(generated, cv2.COLOR_BGR2GRAY)
    mse_num = mse(origin,generated)
    mse_sum+=mse_num
    ssim_num = ssim(origin, generated)
    ssim_sum += ssim_num
    f.write("MSE: "+str(mse_num)+" SSIM: "+ str(ssim_num)+"\n")
    num_images+=1
f.write("MSE Average: "+str(mse_sum/num_images)+" SSIM Average: "+ str(ssim_sum/num_images)+"\n")
f.close()