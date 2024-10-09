import os
from PIL import Image
from collections import Counter

def findMaxWidth(path):
    images_name = os.listdir(path)
    max_width = -1
    for image_name in images_name:
        image = Image.open(f'{path}/{image_name}')
        size = image.size
        if size[0] > max_width:
            max_width = size[0]
    return max_width

def resizeImage(image, width, aspect_ratio):
    height = int(aspect_ratio * width)
    image = image.resize((width, height))
    return image

def findMaxQuantitiOfAspestRatio(input_path):
    images_name = os.listdir(input_path)
    aspect_ratio_arr= []
    
    for image_name in images_name:
            image = Image.open(f'{input_path}/{image_name}')
            size = image.size
            aspect_ratio = size[1] / size[0]
            aspect_ratio_arr.append(aspect_ratio)
    counter = Counter(aspect_ratio_arr)
    return counter.most_common(1)[0][0]

def resizeAllImages(input_path, output_path, aspect_ratio, width=-1, type_of_resize = 0): # type_of_resize == 0 - самое строего / 1 - только по соотношению сторон / 2 - только по ширине / 3 - без ограничений / 4 - все с одной шириной, но с разным соотношением сторон / 5 - все с одним соотношением сторон, но разной шириной
    images_name = os.listdir(input_path)
    not_resize_images = []
    if width == -1:
        width = findMaxWidth(input_path)
    for image_name in images_name:
        image = Image.open(f'{input_path}/{image_name}')
        size = image.size
        if type_of_resize == 0:
            if width > size[0]/2 and aspect_ratio == size[1]/size[0]:
                resized_image = resizeImage(image, width, aspect_ratio)
                resized_image.save(f"{output_path}/{image_name}")
            else:
                not_resize_images.append(image_name)
        elif type_of_resize == 1:
            if aspect_ratio == size[1]/size[0]:
                resized_image = resizeImage(image, width, aspect_ratio)
                resized_image.save(f"{output_path}/{image_name}")
            else:
                not_resize_images.append(image_name)
        elif type_of_resize == 2:
            if width > size[0]/2:
                resized_image = resizeImage(image, width, aspect_ratio)
                resized_image.save(f"{output_path}/{image_name}")
            else:
                not_resize_images.append(image_name)
        elif type_of_resize == 3:
            resized_image = resizeImage(image, width, aspect_ratio)
            resized_image.save(f"{output_path}/{image_name}")
        elif type_of_resize == 4:
            resized_image = resizeImage(image, width, size[1]/size[0])
            resized_image.save(f"{output_path}/{image_name}")
        elif type_of_resize == 4:
            resized_image = resizeImage(image, size[0], aspect_ratio)
            resized_image.save(f"{output_path}/{image_name}")

    return not_resize_images
