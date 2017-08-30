import os
from PIL import Image
import random
from utils.logger import logger
from utils.create_folder import create_folder
from utils.clean_up_folder import clean_up_folder
from utils.compress_image import compress_image


def linear_quality_search(image_path, output_dir, target_val, subsampling=1, image_format='JPEG'):

    random_hash = random.randint(100000, 600001)
    temp_dir = os.path.abspath(output_dir) + '/_temp_' + str(random_hash)
    best_quality = -1

    try:

        cur_size = original_size = os.stat(image_path).st_size / 1000
        best_quality = 90
        dir_path, file_name = os.path.split(image_path)
        name, ext = file_name.split('.')
        temp_file = temp_dir + '/' + name + '_' + str(random_hash) + '.' + ext

        if not create_folder(temp_dir):
            return -1

        while cur_size > target_val:
            
            compress_image(image_path, temp_file, quality=best_quality, image_format=image_format)
            size = os.stat(temp_file).st_size / 1000
            
            if size >= cur_size and not size >= original_size:
                best_quality += 1
                break
            else:
                cur_size = size
                best_quality -= 1


    except Exception as e:
        logger('linear_quality_search', e)
        return -1

    finally:
        if(os.path.isdir(temp_dir)):
            clean_up_folder(temp_dir)

    return best_quality