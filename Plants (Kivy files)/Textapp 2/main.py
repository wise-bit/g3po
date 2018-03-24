import kivy
kivy.require("1.9.0")
from kivy.properties import NumericProperty

from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty

class CustomWidget(Widget):
    last_name_text_input = ObjectProperty()
    ego = NumericProperty(0)
    surname = ''

    def submit_surname(self):
        surname = self.last_name_text_input.text

class CustomWidgetApp(App):
    def build(self):
        return CustomWidget()

customWidget = CustomWidgetApp()
customWidget.run()