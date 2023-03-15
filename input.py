from kivy.uix.screenmanager import Screen
import time
from kivy.properties import Clock
from kivy.uix.textinput import TextInput


class InputScreen(Screen):

	def on_enter(self, *args):
		#self.ids._dalinput_terug.text = "0"
		self.ids._dalinput14.focus = True
		#self.ids._normaalinput_terug.text = "0"

		self.currenttime = time.strftime("%X")
		self.datum = time.strftime("%d-%m-%Y")
		self.ids._tijdstip.text = "time  " + self.currenttime[0:5]
		Clock.schedule_interval(self.timeupdate, 60)
		self.ids._datum.text = self.datum

	def timeupdate(self, *args):
		self.currenttime = time.strftime("%X")
		self.ids._tijdstip.text = "Time "+ self.currenttime[0:5]

	def on_leave(self):
		self.ids._dalinput14.text = "";self.ids._dalinput24.text = "";self.ids._dalinput34.text = "";self.ids._dalinput44.text = ""
		self.ids._normaalinput15.text = "";self.ids._normaalinput25.text = "";self.ids._normaalinput35.text = "";self.ids._normaalinput45.text = "";self.ids._normaalinput55.text = ""
		self.ids._dalinput_terug14.text = "0";self.ids._dalinput_terug24.text = "0";self.ids._dalinput_terug34.text = "0";self.ids._dalinput_terug44.text = "0"
		self.ids._normaalinput_terug15.text = "0";self.ids._normaalinput_terug25.text = "0";self.ids._normaalinput_terug35.text = "0";self.ids._normaalinput_terug45.text = "0";self.ids._normaalinput_terug55.text = "0"
		self.ids. _gasinput14.text = "";self.ids. _gasinput24.text = "";self.ids. _gasinput34.text = "";self.ids. _gasinput44.text = ""

	def insert_text(self, substring, from_undo=False):
		if len(substring) < 2 :  #  if the length of the substring is less than 1, return the substring
				s = substring
				print(s)
		else:
				s = substring[0:1]  # is the substring length is 1 or greater, only return the first 10 characters
				print (s)
		#return super().insert_text(s, from_undo=from_undo)
