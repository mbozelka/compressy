import kivy
kivy.require('1.10.0')

from kivy.uix.screenmanager import Screen
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.properties import ObjectProperty


class OutputSelect(Label):

    def on_touch_down(self, touch):
        if self.collide_point(touch.x, touch.y):
            self.compressor_screen.manager.transition.direction = 'left'
            self.compressor_screen.manager.current = 'folderselector'
        return super(OutputSelect, self).on_touch_down(touch)

class ClearSelectedImages(Label):

    def on_touch_down(self, touch):
        if self.collide_point(touch.x, touch.y):
            self.compressor_screen.manager.files = []
        return super(ClearSelectedImages, self).on_touch_down(touch)

class CompressorScreen(Screen):
    pass