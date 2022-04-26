# import the necessary packages
from skimage.metrics import structural_similarity as ssim
import matplotlib.pyplot as plt
import numpy as np
import cv2
import os
from PIL import Image, ImageChops
import os
def mse(imageA, imageB):
	# the 'Mean Squared Error' between the two images is the
	# sum of the squared difference between the two images;
	# NOTE: the two images must have the same dimension
	err = np.sum((imageA.astype("float") - imageB.astype("float")) ** 2)
	err /= float(imageA.shape[0] * imageA.shape[1])
	
	# return the MSE, the lower the error, the more "similar"
	# the two images are
	return err
def compare_images(imageA, imageB, title):
	# compute the mean squared error and structural similarity
	# index for the images
	m = mse(imageA, imageB)
	s = ssim(imageA, imageB)
	# setup the figure
	fig = plt.figure(title)
	plt.suptitle("MSE: %.2f, SSIM: %.2f" % (m, s))
	# show first image
	ax = fig.add_subplot(1, 2, 1)
	plt.imshow(imageA, cmap = plt.cm.gray)
	plt.axis("off")
	# show the second image
	ax = fig.add_subplot(1, 2, 2)
	plt.imshow(imageB, cmap = plt.cm.gray)
	plt.axis("off")
	# show the images
	plt.show()

# load the images -- the original, the original + contrast,
# and the original + photoshop
original = cv2.imread("./pytorch-CycleGAN-and-pix2pix/results/colored/all/679/Original.png")
contrast = cv2.imread("./pytorch-CycleGAN-and-pix2pix/results/colored/all/679/MSE2.png")
shopped = cv2.imread("./pytorch-CycleGAN-and-pix2pix/results/colored/all/679/SR.png")
# convert the images to grayscale
original = cv2.cvtColor(original, cv2.COLOR_BGR2GRAY)
contrast = cv2.cvtColor(contrast, cv2.COLOR_BGR2GRAY)
shopped = cv2.cvtColor(shopped, cv2.COLOR_BGR2GRAY)
original = cv2.imread("./pytorch-CycleGAN-and-pix2pix/results/colored/all/679/Original.png",cv2.IMREAD_GRAYSCALE )
contrast = cv2.imread("./pytorch-CycleGAN-and-pix2pix/results/colored/all/679/MSE2.png",cv2.IMREAD_GRAYSCALE )
print (mse(original,contrast))
# initialize the figure
# fig = plt.figure("Images")
# images = ("Original", original), ("Contrast", contrast), ("Photoshopped", shopped)
# # loop over the images
# for (i, (name, image)) in enumerate(images):
# 	# show the image
# 	ax = fig.add_subplot(1, 3, i + 1)
# 	ax.set_title(name)
# 	plt.imshow(image, cmap = plt.cm.gray)
# 	plt.axis("off")
# # show the figure
# plt.show()
# compare the images
# compare_images(original, original, "Original vs. Original")
# compare_images(original, contrast, "Original vs. MSE")
# compare_images(original, shopped, "Original vs. SR")

#MSE lower more similiar
#SSIM higher more similiar

#MSE 
# test = "./pytorch-CycleGAN-and-pix2pix/results/colored/MSE/MSE/test_latest/images/"
#L1
save_path = "./pytorch-CycleGAN-and-pix2pix/results/colored/colored/test_latest/images/"

#writes differences to file
f = open(save_path+"L1_analysis.txt", "w")
mse_sum=0
ssim_sum=0
num_images=0
nums = [10,13,138,679,1488,4938,5008,6799,7246,7271,9992,9998]
for num in nums:
    origin = cv2.imread(os.path.join(save_path, str(num)+ "_real_B.png"), cv2.IMREAD_GRAYSCALE)
    generated = cv2.imread(os.path.join(save_path, str(num) + "_fake_B.png"),cv2.IMREAD_GRAYSCALE)
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