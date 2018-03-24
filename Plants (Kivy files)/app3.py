import kivy
kivy.require('1.0.0')
from kivy.uix.textinput import TextInput

from kivy.app import App
from kivy.uix.button import Button

class MyApp(App):

    def on_enter(instance, value):
        print('User pressed enter in', instance)

    def build(self):
        # return Button(text='Hello World')

        textinput = TextInput(text='Hello world')
        return Button(text=textinput)

if __name__ in ('__android__', '__main__'):
    MyApp().run()