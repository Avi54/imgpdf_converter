from PIL import Image
from os import walk, path

dir_path = input('directory path (images location): ')
save_path = input('directory path for saving: ') 
pdf_name = input('file name: ') + '.pdf'

images_list = []
for root, dirs, files in walk(path.abspath(dir_path)):
    for file in files:
        image_path = path.join(root, file)
        img = Image.open(image_path)
        images_list.append(img.convert('RGB'))

first_image = images_list[0]
del images_list[0]

first_image.save(path.join(save_path, pdf_name), save_all=True, append_images=images_list) 