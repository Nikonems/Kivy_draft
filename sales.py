from kivy.app import App
from kivy.uix.widget import Widget
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen 
import pandas as pd
from openpyxl.workbook import Workbook
from kivy.uix.textinput import TextInput
import datetime as dt


#Define our different screens
class FirstWindow(Screen):


	def press2(self):
		#with pd.ExcelWriter(r'C:\Users\79254\kivy_project\ex1.xlsx',
							#mode="a",
							#engine="openpyxl",
							#if_sheet_exists='overlay') as writer:

		import pathlib
		import pathlib
		from pathlib import Path

		# Получаем строку, содержащую путь к домашней директории:
		dir_path = pathlib.Path.home()

		# Объединяем полученную строку с недостающими частями пути
		path = Path(dir_path, 'kivy_project', 'ex1.csv')
		AwesomeApp.get_running_app().df.to_csv(path,mode='a',header=False)


		#'ex_{}.xlsx'.format(dt.datetime.now().strftime('%d%m%y_%H%M%S')))
		print(f'ex added')


class SecondWindow(Screen):

	def __init__(self, **kwargs):
		# Call grid layout constructor
		super(SecondWindow, self).__init__(**kwargs)
		self.counter = 0



	def press(self):

		count = self.ids.count.text

		# Add widgets


		#print(f'Hello {name}, you like {pizza} pizza, and your favorite color is {color}!')
		# Print it to the screen

		self.counter= self.counter + int(count)


		df1=pd.DataFrame({'продукт':'самса','количество':[count],'время продажи':dt.datetime.now(),'количество всего':[self.counter], })
		AwesomeApp.get_running_app().df=pd.concat([AwesomeApp.get_running_app().df,df1])
		self.ids.count.text=''

class WindowManager(ScreenManager):
	pass

# Designate Our .kv design file 
kv = Builder.load_file('sales.kv')


class AwesomeApp(App):
	df = pd.DataFrame(columns=['продукт','количество', 'время продажи','количество всего'])
	def build(self):
		return kv

if __name__ == '__main__':
	AwesomeApp().run()



