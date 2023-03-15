from kivy.app import App
from kivy.config import Config
Config.set('graphics', 'width',350)
Config.set('graphics', 'height',700)
Config.set('graphics', 'resizable',1)
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager
from kivy.uix.popup import Popup
from kivy.uix.label import Label
from kivy.properties import StringProperty,ListProperty

Builder.load_file('welcome.kv')
Builder.load_file('menu.kv')
Builder.load_file('input.kv')
Builder.load_file('stats.kv')
Builder.load_file('analyse.kv')
Builder.load_file('settings.kv')

class EnergyControlScreens(ScreenManager):
	pass


class MainApp(App):

	def build(self):
		return EnergyControlScreens()

if __name__ == '__main__':

	MainApp().run()
