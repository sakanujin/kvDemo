# -*- coding: utf-8 -*
import os
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.boxlayout import BoxLayout

from kivy.properties import StringProperty
######################################
from kivy.core.window import Window
from kivy.factory import Factory
######################################
from kivy.uix.togglebutton import ToggleButton # for toggle

##################### jap font ############
from kivy.core.text import LabelBase, DEFAULT_FONT
from kivy.resources import resource_add_path

resource_add_path('{}\\{}'.format(os.environ['SYSTEMROOT'], 'Fonts'))
LabelBase.register(DEFAULT_FONT, 'MSGOTHIC.ttc')

# load kv file one by one
from kivy.lang import Builder

##########################################################################
class TextWidget(Widget):
    text = StringProperty()
    text2 = StringProperty()
    text3 = StringProperty()
    set_temp = 0
    temp     = str(set_temp)

    def __init__(self, **kwargs):
        super(TextWidget, self).__init__(**kwargs)
        self.text = 'オフ'
        self.text2 = 'UP'
        self.text3 = 'DOWN'

    def buttonClicked(self):  
        self.text = "オン"
        self.temp = str(self.set_temp)
        if self.text == "オン":
            #self.text = "オフ"
            self.text == "オン"
        else :
            self.text == "オン"

        print ("self.temp is ", self.temp)

    def btc2(self):  
        self.text2 = "UP++"
        self.set_temp = self.set_temp + 1
        self.temp  = str(self.set_temp)

    def btc3(self):  
        self.text3 = "DOWN--"
        self.set_temp = self.set_temp - 1
        self.temp = str(self.set_temp)

class TestApp(App):

    def __init__(self, **kwargs):
        super(TestApp, self).__init__(**kwargs)
        self.title = 'freezer UI/UX'

    def build(self):
        return TextWidget()


##########################################################################

Builder.load_file('window1.kv')
Builder.load_file('window2.kv')

class MainRoot(BoxLayout):
    text3   = "saka"
    window1 = None
    window2 = None
    set_temp = 0
    tmp = str(set_temp)

    def __init__(self, **kwargs):
        self.window1 = Factory.Window1()
        self.window2 = Factory.Window2()
        super(MainRoot, self).__init__(**kwargs)

    def change_disp(self):
        self.clear_widgets()
        self.add_widget(self.window1)

    def change_disp2(self):
        self.clear_widgets()
        self.add_widget(self.window2)

    def buttonClicked(self):  
        self.text = "オン"
        if self.text == "オン":
            self.text == "オン"
        else :
            self.text == "オン"

    def btc2(self):  
        self.text2 = "UP++"
        self.set_temp = self.set_temp + 1
        self.temp  = str(self.set_temp)

    def btc3(self):  
        self.text3 = "DOWN--"
        self.set_temp = self.set_temp - 1
        self.temp = str(self.set_temp)


class MainApp(App):
    def __init__(self, **kwargs):
        super(MainApp, self).__init__(**kwargs)
        self.title = 'state transition Test'
    pass   

   # def build(self):
   #     return TextWidget()

if __name__ == "__main__":
    MainApp().run()





#if __name__ == "__main__":
#    TestApp().run()
