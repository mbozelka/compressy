
import kivy
kivy.require('1.10.0')

import os
from kivy.core.window import Window
from kivy.uix.screenmanager import Screen
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import ObjectProperty
from kivy.properties import BooleanProperty
from imagecompressthread import ImageCompressThread

class CompressionDetailsScreen(Screen):

    clean_up_thread_count = 0
    process_complete = BooleanProperty(False)
    details_output = ObjectProperty(None)
    ui_list = []

    def __init__(self, **kwargs):
        super(CompressionDetailsScreen, self).__init__(**kwargs)
        Window.bind(on_resize=self._update_ui)
        
    def on_enter(self):
        self.process_complete = False
        clean_up_thread_count = 0
        self.ui_list = []
        self._buildUI()
        self._comrpess_images()

    def on_pre_leave(self):
        manager = self.manager
        manager.out_put_directory_selected = False
        manager.out_put_directory = manager.default_messages['OUTPUT_FOLDER']
        manager.files = []
        for widget in self.ui_list:
            self.details_output.remove_widget(widget)

    def _comrpess_images(self):
        manager = self.manager
        mode_quality = manager.percent_val if manager.compress_mode == manager.compress_mode_enum['PERCENT'] else manager.kb_val
        
        for i in range(0, len(manager.files)):
            ic_thread = ImageCompressThread(thread_num=i, image_path=manager.files[i], output_dir=manager.out_put_directory, 
                mode_quality=mode_quality, mode=manager.compress_mode, notify_func=self._thread_update)
            ic_thread.start()

    def _thread_update(self, index, msg):
        manager = self.manager
        self.ui_list[index].children[1].text = msg

        if msg == 'Success':
            self.clean_up_thread_count += 1

        if len(self.ui_list) == self.clean_up_thread_count:
            self.process_complete = True


    def _buildUI(self):
        manager = self.manager
        color = [.16, .17, .18, 1]

        for i in range(0, len(manager.files)):
            
            dir_path, file_name = os.path.split(manager.files[i])
            output = manager.out_put_directory + '/' + file_name

            layout = BoxLayout(
                size_hint= (1, .05),
                padding=10,
                spacing=5
            )
            
            sl = Label(
                size_hint= (.2, 1),
                text='Waiting',
                color=color,
                markup= True,
                shorten= True,
                shorten_from= 'right',
                max_lines= 1,
                text_size= (self.width * .2, None),
                ellipsis_options= {'color':color}
            )

            dl = Label(
                size_hint= (.8, 1),
                text=output,
                color=color,
                markup= True,
                shorten= True,
                shorten_from= 'left',
                max_lines= 1,
                text_size= (self.width * .8, None),
                ellipsis_options= {'color':color}
            )

            layout.add_widget(sl)
            layout.add_widget(dl)
            layout.pos_hint = {'x':0, 'y': .90 - (i * .05)}

            self.details_output.add_widget(layout)
            self.ui_list.append(layout)


    def _update_ui(self, obj, width, height):
        for text in self.ui_list:
            text.children[0].text_size = (width * .8, None)
            text.children[1].text_size = (width * .2, None)
