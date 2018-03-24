from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.properties import NumericProperty, ObjectProperty
from kivy.lang import Builder
from kivy.uix.textinput import TextInput


class ThemeBackground(Screen):
    myslider = ObjectProperty(None)
    texttt = TextInput(text='Hello world', multiline=False)

class myApp(App):
    def build(self):
        self.load_kv("my.kv")
        tb = ThemeBackground() 
        textt = tb.texttt
        print("value =",tb.myslider.value) # <---- value here
        # print("min =",tb.myslider.min) # <--- min here
        return tb

if __name__ == '__main__':
    myApp().run()