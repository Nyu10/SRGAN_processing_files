
# import module
from PIL import Image, ImageChops
import os

#https://www.geeksforgeeks.org/spot-the-difference-between-two-images-using-python/


# test = "./pytorch-CycleGAN-and-pix2pix/results/colored/all/679"
# path = './pytorch-CycleGAN-and-pix2pix/results/mediumCheck2.0/medicalPix2Pix/test_latest/images'
# save_path = './dataset/1000officialtest/difference/'

# for image in os.listdir(test):
#     origin = Image.open(os.path.join(path, image[:-5] + "_real_B.png"))
#     generated = Image.open(os.path.join(path, image[:-5] + "_fake_B.png"))
#     diff = ImageChops.difference(origin, generated)
#     diff.save(os.path.join(save_path + image[:-5] + "_difference.png"))

test = "./pytorch-CycleGAN-and-pix2pix/results/colored/all/679"
save_path = "./pytorch-CycleGAN-and-pix2pix/results/colored/all/679/difference"

origin = Image.open(os.path.join(test, "Original.png"))
generated = Image.open(os.path.join(test, "MSE2.png"))
diff = ImageChops.difference(origin, generated)
diff.save(os.path.join(save_path, "MSE2_difference.png"))