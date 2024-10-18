import os
from PIL import Image, ImageOps
from collections import Counter
import math

def findMaxWidth(path): # максимальная длинная изображения в папке
    images_name = os.listdir(path)
    max_width = -1
    for image_name in images_name:
        image = Image.open(f'{path}/{image_name}')
        size = image.size
        if size[0] > max_width:
            max_width = size[0]
    return max_width

def resizeImage(image, width, height): # изменить размер изображения
    # size = image.size
    # if not(width/size[0] < 2 or width*aspect_ratio/size[1] < 2 or width/size[0] > 0.5 or width*aspect_ratio/size[1] < 0.5):
    image = image.resize((width, height))
    return image


def findMaxQuantitiOfAspestRatio(input_path): # найти само часто встречающиеся соотношение сторон
    images_name = os.listdir(input_path)
    aspect_ratio_arr= []
    
    for image_name in images_name:
            image = Image.open(f'{input_path}/{image_name}')
            size = image.size
            aspect_ratio = size[1] / size[0]
            aspect_ratio_arr.append(aspect_ratio)
    counter = Counter(aspect_ratio_arr)
    return counter.most_common(1)[0][0]

def resizeAllImages(input_path, output_path, edge_color):
    images_name = os.listdir(input_path)
    not_resize_images = []
    
    for image_name in images_name:
        image = Image.open(f'{input_path}/{image_name}')
        size = image.size
        normal_size = detTheBestWidth(size)
        width = normal_size[0]
        height = normal_size[1]
        file_name_without_ext = os.path.splitext(image_name)[0]
        
        # if type_of_resize == 0:
        #     if width > size[0] / 2 and aspect_ratio == size[1] / size[0]:
        #         resized_image = resizeImage(image, width, aspect_ratio)
        #         resized_image = processImage(resized_image, edge_color, findGoodEdgePlacement(resized_image))
        #         if resized_image is not None:
        #             resized_image.save(f"{output_path}/{file_name_without_ext}.jpg")
        #         else:
        #             not_resize_images.append(image_name)
                    
        # if type_of_resize == 1:
        #     if aspect_ratio == size[1] / size[0]:
        #         resized_image = resizeImage(image, width, aspect_ratio)
        #         if resized_image is not None:
        #             resized_image = processImage(resized_image, edge_color, findGoodEdgePlacement(resized_image))
        #             if resized_image is not None:
        #                 resized_image.save(f"{output_path}/{file_name_without_ext}.jpg") # tiff ужастно выглядит
        #             else:
        #                 not_resize_images.append(image_name)
        #         else:
        #                 not_resize_images.append(image_name)
                    
        # elif type_of_resize == 2:
        #     if width > size[0] / 2:
        #         resized_image = resizeImage(image, width, aspect_ratio)
        #         resized_image = processImage(resized_image, edge_color, findGoodEdgePlacement(resized_image))
        #         if resized_image is not None:
        #             resized_image.save(f"{output_path}/{file_name_without_ext}.jpg")
        #         else:
        #             not_resize_images.append(image_name)
                    
        # elif type_of_resize == 3:
        #     resized_image = resizeImage(image, width, aspect_ratio)
        #     if resized_image is not None:
        #         resized_image = processImage(resized_image, edge_color, findGoodEdgePlacement(resized_image))
        #         if resized_image is not None:
        #             resized_image.save(f"{output_path}/{file_name_without_ext}.jpg") 
        #         else:
        #             not_resize_images.append(image_name)
        #     else:
        #             not_resize_images.append(image_name)
        print(image_name)
        if width !=-1 and height != -1:
            resized_image = resizeImage(image, width, height)
            resized_image = processImage(resized_image, edge_color, findGoodEdgePlacement(resized_image))
            resized_image.save(f"{output_path}/{file_name_without_ext}.jpg")
        else:
            not_resize_images.append(image_name)
                
        # elif type_of_resize == 5:
        #     resized_image = resizeImage(image, size[0], aspect_ratio)
        #     if resized_image is not None:
        #         resized_image = processImage(resized_image, edge_color, findGoodEdgePlacement(resized_image))
        #         if resized_image is not None:
        #             resized_image.save(f"{output_path}/{file_name_without_ext}.jpg")
        #         else:
        #             not_resize_images.append(image_name)
        #     else:
        #         not_resize_images.append(image_name)

    return not_resize_images


# ====================================================================


def processImage(image, edge_color, edge_placement): # приведение изображения к А4
    A4_SIZE = (2480, 3508) # при dpi300 и соотношение сторон a4 210/297
    
    
    if edge_placement == "all_sides": # все стороны
        new_image = ImageOps.expand(image, border=((A4_SIZE[0] - image.size[0]) // 2, (A4_SIZE[1] - image.size[1]) // 2), fill=edge_color)
        new_image =  new_image.convert('CMYK')
    elif edge_placement == "top_bottom": #сверху снизу
        new_image = ImageOps.expand(image, border=(0, (A4_SIZE[1] - image.size[1]) // 2), fill=edge_color)
        new_image =  new_image.convert('CMYK')
    elif edge_placement == "left_right": # слева страва 
        new_image = ImageOps.expand(image, border=((A4_SIZE[0] - image.size[0]) // 2, 0), fill=edge_color)
        new_image =  new_image.convert('CMYK')
    elif edge_placement == "no_where": # нигде 
        new_image = image
        new_image =  new_image.convert('CMYK')


    return new_image

def findGoodEdgePlacement(image):
    size = image.size
    A4_SIZE = (2480, 3508)
    if size[0] < A4_SIZE[0] and size[1] < A4_SIZE[1]:
        edge_placement = "all_sides"
    elif size[1]/size[0] > A4_SIZE[1]/A4_SIZE[0]:
        edge_placement = "left_right"
    elif size[1]/size[0] < A4_SIZE[1]/A4_SIZE[0]:
        edge_placement = "top_bottom"
    elif size[1]/size[0] == A4_SIZE[1]/A4_SIZE[0]:
        edge_placement = "no_where"
    return edge_placement

def detTheBestWidth(size): # определение максимального изменения разрешения изображения без уменьшения / улевичения в 2 раза
    A4_SIZE = (2480, 3580)
    width_min_max = (1754, 3507) # ширина А4 *2^0.5 || ширина А4 /2^0.5
    height_min_max = (2478, 5062) # аналогично высота
    if A4_SIZE[0] == size[0]:
        width = size[0]
    elif A4_SIZE[0] < size[0]:
        if size[0] <= width_min_max[1]:
            width = A4_SIZE[0]
        else:
            width = -1
    elif A4_SIZE[0] > size[0]:
        if size[0] >= width_min_max[0]:
            width = A4_SIZE[0]
        elif size[0] * math.sqrt(2) >= width_min_max[0]:
            width = int(size[0] * math.sqrt(2))
        else:
            width = -1


    if A4_SIZE[1] == size[1]:
        height = size[1]
    elif A4_SIZE[1] < size[1]:
        if size[1] <= height_min_max[1]:
            height = A4_SIZE[1]
        else:
            height = -1
    elif A4_SIZE[1] > size[1]:
        if size[1] >= height_min_max[0]:
            height = A4_SIZE[1]
        elif size[1] * math.sqrt(2) >= height_min_max[0]:
            height = int(size[1] * math.sqrt(2))
        else:
            height = -1

    normal_size = (width, height)
    print(normal_size)
    return normal_size
