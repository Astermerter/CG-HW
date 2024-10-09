from PIL import Image, ImageOps
import os
import subfunc


input_path = 'input_images'
output_path = 'output_images'
not_resize_images = subfunc.resizeAllImages(input_path, output_path, subfunc.findMaxQuantitiOfAspestRatio(input_path), type_of_resize=4, width=250)

# images_name = os.listdir(input_path)
# print(images_name)
# max_width = subfunc.findMaxWidth(path)

# for image_name in images_name:
#     image = Image.open(f'{path}/{image_name}')
#     size= image.size
#     format = image.format
#     aspect_ratio = size[1]/size[0]
    # print(image.format, image.size, image_name)


