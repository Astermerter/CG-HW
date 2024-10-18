from PIL import Image, ImageOps, ImageColor
import os
import subfunc


input_path = 'input_images'
output_path = 'output_images'
edge_color = ImageColor.getrgb("#FF0000")
# not_resize_images = subfunc.resizeAllImages(input_path, output_path, edge_color= edge_color)

# image = Image.open(f'{input_path}/image.png')
# image = Image.open("C:/Users/sosni/OneDrive/Рабочий стол/тестовый прогон/манул.jpeg")
# image = image.resize((1500, 2000))
# image.save("C:/Users/sosni/OneDrive/Рабочий стол/тестовый прогон/манул good.jpg")
# size = (626, 533)
# A4_SIZE = (2480, 3508)

# new_image = ImageOps.expand(image, border=((A4_SIZE[0] - image.size[0]) // 2, (A4_SIZE[1] - image.size[1]) // 2), fill=edge_color)
# new_image =  new_image.convert('CMYK')
# new_image.save(f'{output_path}/image.jpg')
# images_name = os.listdir(input_path)
# print(images_name)
# max_width = subfunc.findMaxWidth(path)

# for image_name in images_name:
#     image = Image.open(f'{input_path}/{image_name}')
#     print(os.path.basename(image.filename))
#     size= image.size
    # image = image.resize(size=(5000, 8000))
    # image.save(f"{output_path}/{image_name}")
#     format = image.format
#     aspect_ratio = size[1]/size[0]
    # print(image.format, image.size, image_name)


