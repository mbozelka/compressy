import kivy
kivy.require('1.10.0')

from kivy.clock import mainthread
from kivy.uix.relativelayout import RelativeLayout
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty

class SlidersView(RelativeLayout):
    
    # properties
    percent_slider = ObjectProperty(None)
    percent_toggle = ObjectProperty(None)
    percent_label = ObjectProperty(None)

    kb_slider = ObjectProperty(None)
    kb_toggle = ObjectProperty(None)
    kb_label = ObjectProperty(None)

    def __init__(self, **kwargs):
        super(SlidersView, self).__init__(**kwargs)
        @mainthread
        def delayed():
            cs = self.compressor_screen.manager

            self.percent_toggle.bind(active=self.on_percent_toggle)
            self.percent_slider.bind(value=self.slider_val_change)

            self.kb_toggle.bind(active=self.on_kb_toggle)
            self.kb_slider.bind(value=self.slider_val_change)

            cs.kb_val = self.kb_slider.value
            cs.percent_val = self.percent_slider.value
            self.percent_toggle.active = True

        delayed()

    def slider_val_change(self, obj, value):
        cs = self.compressor_screen.manager

        if obj == self.percent_slider:
            cs.percent_val = int(value)
        else:
            cs.kb_val = int(value)

    def on_percent_toggle(self, obj, value):
        if value == True:
            cs = self.compressor_screen.manager
            self.percent_slider.disabled = False
            self.percent_label.disabled = False
            self.kb_slider.disabled = True
            self.kb_label.disabled = True
            cs.compress_mode = cs.compress_mode_enum['PERCENT']

    def on_kb_toggle(self, obj, value):
        if value == True:
            cs = self.compressor_screen.manager
            self.percent_slider.disabled = True
            self.percent_label.disabled = True
            self.kb_slider.disabled = False
            self.kb_label.disabled = False
            cs.compress_mode = cs.compress_mode_enum['KB']