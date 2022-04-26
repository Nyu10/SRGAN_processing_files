import cv2
import numpy as np
from PIL import Image
import os




def image_resize(image, width=None, height=None, inter=cv2.INTER_AREA):
    # initialize the dimensions of the image to be resized and
    # grab the image size
    dim = None
    (h, w) = image.shape[:2]

    # if both the width and height are None, then return the
    # original image
    if width is None and height is None:
        return image

    # check to see if the width is None
    if width is None:
        # calculate the ratio of the height and construct the
        # dimensions
        r = height / float(h)
        dim = (int(w * r), height)

    # otherwise, the height is None
    else:
        # calculate the ratio of the width and construct the
        # dimensions
        r = width / float(w)
        dim = (width, int(h * r))

    # resize the image
    resized = cv2.resize(image, dim, interpolation=inter)

    # return the resized image
    return resized


# path0 = "./dataset/raw/train/"
# path1 = "./dataset/256raw/train/"
# path0 = "./dataset/processed/train/"
# path1 = "./dataset/256blurry/train/"
path0 = "../../../Desktop/original"
path1 = "../../../Desktop/small_original/"
dirs = os.listdir( path0 )
def load_images_from_folder(folder):
    for filename in os.listdir(folder):
        img = cv2.imread(os.path.join(folder,filename))
        # img = image_resize(img, height=512)
        h, w, _ = img.shape
        h=h//4
        img = image_resize(img, height=h)
        cv2.imwrite(os.path.join(path1,filename), img)
images = load_images_from_folder(path0)




# file = './dataset/test/test/0AA9XP3MFSEX_0_1568.tiff'
# img = cv2.imread(file, 0)
# print(img.shape)
# img = image_resize(img, height = 256)
# cv2.imwrite(file, img)

