from PIL import Image
from IPython.display import display
import os


path = "./dataset/colored/train/"
save_path_LR = "../../../Desktop/A/"
save_path_HR = "../../../Desktop/B/"
dirs = os.listdir(path)

# 0 1 2 3 
interval = 3
start = 2500 * interval + 1
end = start + 2500
def split_images(folder):
    for num in range (start, end):
        filename = str(num) + ".tif"
        # img = Image.open(os.path.join(folder, dirs[num]))
    # for filename in os.listdir(folder):
        img = Image.open(os.path.join(folder, filename))
        LR = img.crop((0, 0, img.width//2, img.height))
        HR = img.crop((img.width//2, 0, img.width, img.height))
        # pixels = img.load()  # creates the pixel map
        # for i in range(0, 513):
        #     for j in range(0, 513):
        #         pixels[i,i] = (0, 0, 0)
        # for i in range(0, 513):
        #     for j in range(513, 1025):
        #         pixels[i,j] = (0, 0, 0)
        LR.save(os.path.join(save_path_LR, filename))
        HR.save(os.path.join(save_path_HR, filename))
        img.close()
        LR.close()
        HR.close()
        if (num % 500 == 0):
            print ("finished " + str(num))
        # img.save(os.path.join(path, filename))


split_images(path)
