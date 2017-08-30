import kivy
kivy.require('1.10.0')

from kivy.config import Config
Config.set('kivy', 'desktop', 1)
Config.set('graphics','width','600')
Config.set('graphics','height','450')

from kivy.app import App
from kivy.core.window import Window
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager
from kivy.properties import StringProperty
from kivy.properties import BooleanProperty
from kivy.properties import ListProperty
from kivy.properties import NumericProperty
from utils.compressmodeenum import CM_ENUM
from utils.logger import logger
from utils.defaultmessagesenum import DEFAULT_MESSAGES

Builder.load_file('appscreenmanager.kv')
Builder.load_file('compressorscreen.kv')
#Builder.load_file('detailscreen.kv')
Builder.load_file('folderselectorscreen.kv')
Builder.load_file('slidersview.kv')
Builder.load_file('dragdropview.kv')
Builder.load_file('compressiondetailsscreen.kv')


class AppScreenManager(ScreenManager):
    compress_mode_enum = CM_ENUM
    default_messages = DEFAULT_MESSAGES
    out_put_directory_selected = BooleanProperty(False)
    out_put_directory = StringProperty(default_messages['OUTPUT_FOLDER'])
    files = ListProperty([])
    compress_mode = CM_ENUM['PERCENT']
    percent_val = NumericProperty(0)
    kb_val = NumericProperty(0)

    def __init__(self, **kwargs):
        super(AppScreenManager, self).__init__(**kwargs)


class ImageCompressorApp(App):
    def build(self):
        self.title = 'Compressy'
        return AppScreenManager()

if __name__ == "__main__":
    ImageCompressorApp().run()