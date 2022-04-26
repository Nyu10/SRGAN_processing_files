from PIL import Image
from IPython.display import display
import os


path0 = "./dataset/colored/test/"
path1 = "./dataset/colored_with_small_white_box/test/"
dirs = os.listdir(path0)


def load_images_from_folder(folder):
    for filename in os.listdir(folder):
        img = Image.open(os.path.join(folder, filename))
        pixels = img.load()  # creates the pixel map
        for i in range(236, 277):
            for j in range(236, 277):
                pixels[i, j] = (0, 0, 0)
        for i in range(748, 789):
            for j in range(236, 277):
                pixels[i, j] = (0, 0, 0)
        #small white box
        for i in range(251, 262):
            for j in range(251, 262):
                pixels[i, j] = (255, 255, 255)
        for i in range(763, 774):
            for j in range(251, 262):
                pixels[i, j] = (255, 255, 255)
        img.save(os.path.join(path1, filename))


images = load_images_from_folder(path0)
