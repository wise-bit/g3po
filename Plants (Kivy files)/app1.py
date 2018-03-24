import kivy
kivy.require('1.7.2')
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.label import Label
from kivy.core.window import Window
from kivy.uix.button import Button

from kivy.config import Config
Config.set('graphics','resizable',0) #don't make the app re-sizeable
#Graphics fix
Window.clearcolor = (0,0,0,1.)  #this fixes drawing issues on some phones


#this is the main widget that contains the game
class GUI(Widget):
	def __init__(self, **kwargs):
		super(GUI, self).__init__(**kwargs)
		l = Label(text='Not Your first Kivy App!')
		l.x = Window.width/2 - l.width/2
		l.y = Window.height/2
		self.add_widget(l)

class FractalForm(Widget):
	# ball = ObjectProperty(None)
	button = Button(text='Hello world', font_size=14)

class FractalApp(App):
	def build(self):
		form = FractalForm()
		form.button

		# game.serve_ball()
		# Clock.schedule_interval(form.update, 1.0 / 60.0)
		return form

if __name__ == '__main__':
	FractalApp().run()
