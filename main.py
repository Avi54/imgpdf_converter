from PIL import Image
from os import walk, path

dir_path = input('directory path (images location): ')
save_path = input('directory path for saving: ') 
pdf_name = input('file name: ') + '.pdf'

image_paths = []
for root, dirs, files in walk(path.abspath(dir_path)):
    for file in files:
        image_path = path.join(root, file)
        image_paths.append(image_path)

image_paths.sort()

images_list = []
for file_path in image_paths:
    img = Image.open(file_path)
    images_list.append(img.convert('RGB'))

first_image = images_list[0]
del images_list[0]

first_image.save(path.join(save_path, pdf_name), save_all=True, append_images=images_list) 