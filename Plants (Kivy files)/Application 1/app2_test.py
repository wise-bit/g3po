from kivy.clock import Clock
from kivy.app import App
from kivy.config import Config
from kivy.uix.textinput import TextInput

Config.set('graphics', 'window_state', 'hidden')

class MyDebugApp(App):
    visible = False
    def build(self):
        return TextInput()

    def on_start(self):
        Clock.schedule_interval(self.alternate, 2)
        # self.root.focus = True

    def alternate(self, dt):
        if self.visible:
            self.root_window.hide()
        else:
            self.root_window.show()
            print(self.root_window.focus)

        self.visible = not self.visible


if __name__ == "__main__":
    ma = MyDebugApp().run()