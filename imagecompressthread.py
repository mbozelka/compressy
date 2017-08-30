
import os
import threading
from utils.logger import logger
from utils.linear_quality_search import linear_quality_search
from utils.compress_image import compress_image
from utils.compressmodeenum import CM_ENUM


class ImageCompressThread(threading.Thread):

    compress_mode_enum = CM_ENUM

    def __init__(self, thread_num, image_path, output_dir, mode_quality, mode, notify_func):
        super(ImageCompressThread, self).__init__()
        self.image_path = image_path
        self.output_dir = output_dir
        self.mode_quality = mode_quality
        self.mode = mode
        self.notify_func = notify_func
        self.thread_num = thread_num

    def run (self):
        self._compress_image()

    def _compress_image(self):
        
        self.notify_func(index=self.thread_num, msg='In Progress')

        try:
            dir_path, file_name = os.path.split(self.image_path)
            output = self.output_dir + '/' + file_name
            quality = self.mode_quality

            if not self.mode == self.compress_mode_enum['PERCENT']:
                quality = self._get_best_quality(self.image_path, self.output_dir, quality)

            format = self._map_format(self.image_path)

            compress_image(image_path=self.image_path, output_path=output, quality=quality, image_format=format)
            self.notify_func(index=self.thread_num, msg='Success')

        except Exception as e:
            logger('ImageCompressThread', 'Error in comrpessing image from sub-thread')
            logger('ImageCompressThread', e)
            self.notify_func(index=self.thread_num, msg='Error')


    def _map_format(self, image_path):
        formats = {
            '.jpg' : 'JPEG',
            '.png' : 'PNG',
            '.gif' : 'GIF'
        }
        ext = os.path.splitext(image_path)[1].lower()
        return formats[ext]

    def _get_best_quality(self, image_path, output_dir, quality):
        return linear_quality_search(image_path, output_dir, quality)