import kivy
kivy.require('1.10.0')

import os
from kivy.core.window import Window
from kivy.uix.relativelayout import RelativeLayout
from kivy.properties import StringProperty
from utils.logger import logger

class DragDropView(RelativeLayout):
    def __init__(self, **kwargs):
        super(DragDropView, self).__init__(**kwargs)
        Window.bind(on_dropfile=self._on_file_drop)

    def _on_file_drop(self, window, file_path):
        _cs = self.compressor_screen
        _path = self._extractByteText(file_path)
        _dups = []

        try:

            if os.path.isdir(_path):
                files_list = os.listdir(_path)
                
                for f in files_list:
                    full_path = _path + '/' + f
                    if self._is_dup(full_path):
                        _dups.append(full_path)
                    elif self._isImage(full_path) and not os.path.isdir(full_path):
                        _cs.manager.files.append(full_path)

            else:
                if self._is_dup(_path):
                    _dups.append(_path)
                elif self._isImage(_path):
                    _cs.manager.files.append(_path)

        except  Exception as e:
            logger('DragDropView', e)
            logger('DragDropView', 'error adding images')
            _cs.manager.files_selected = False
            _cs.manager.files = []

        finally:
            if len(_dups) > 0:
                logger('DragDropView', 'Duplicates Ignored')



    def _isImage(self, file_path):
        return os.path.splitext(file_path)[1].lower() in ['.jpg', '.png', '.gif']

    def _extractByteText(self, _bytes):
        return _bytes.decode(encoding="utf-8", errors="strict")

    def _is_dup(self, _path):
        return _path in self.compressor_screen.manager.files
