try:
<<<<<<< HEAD:pandastable/exploredata.py
   from tkinter import *
except ImportError as e:
   from Tkinter import *

=======
	from tkinter import *
except ImportError as e:
	from Tkinter import *
>>>>>>> f046e4bfd7d6b8c84fd53a1518445984028ceca9:pandastable/pandastable_wrapper.py
from pandastable import Table, TableModel
import pandas


class data_explore(Frame):
	"""Basic GUI frame for the table
 		Returns:
		tkinter frame
	"""
	def __init__(self, df):
		self.parent = None
		Frame.__init__(self)
		self.main = self.master
		self.main.geometry('600x400+200+100')
		self.main.title('Explore Data')
		f = Frame(self.main)
		f.pack(fill=BOTH,expand=1)
        #set the table in the GUI
		self.table = pt = Table(f, dataframe=df,
			                    showtoolbar=True, showstatusbar=True)
		pt.show()
		return



#df = pandas.read_csv('./2.csv')
#app = ExploreData(df)

#launch the app
#app.mainloop()


