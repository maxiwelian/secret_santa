from PIL import Image
import os

downloads = "downloads"
for dir in os.listdir(downloads):
    dir = os.path.join(downloads, dir)
    for im_name in os.listdir(dir):
        im_name = os.path.join(dir, im_name)
        try:
            im = Image.open(im_name)
            im.show()
            im = im.convert('LA')
            im.show()
            im = im.resize(28,28)
            im.show()
        except:
            print("fail")
            pass