
import kivy
kivy.require('1.10.0')

from os.path import join, isdir, expanduser
from kivy.uix.screenmanager import Screen
from kivy.properties import ObjectProperty

class FolderSelectorScreen(Screen):

    def is_dir(self, directory, filename):
        return isdir(join(directory, filename))

    def cancel(self):
        self.manager.transition.direction = 'right'
        self.manager.current = 'compressor'

    def save(self, text):
        stripped_str = text.strip()
        is_dir = isdir(stripped_str)
        
        if stripped_str == '' or not is_dir:
            self.manager.out_put_directory_selected = False
            self.manager.out_put_directory = self.manager.default_messages.OUTPUT_FOLDER.value

        elif is_dir:
            self.manager.out_put_directory_selected = True
            self.manager.out_put_directory = text
            self.manager.transition.direction = 'right'
            self.manager.current = 'compressor'


    def get_desktop_path(self):
        return expanduser('~')