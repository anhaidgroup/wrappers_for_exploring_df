<<<<<<< HEAD
from pandastable_wrapper import data_explore
=======
#### PRADAP: MODIFY THIS #######
from exploredata import ExploreData
>>>>>>> 4bc23086cd4ee92a403fcb0cee430c80879a8f65
import pandas
#get the pandas frame from file
df = pandas.read_csv('table.csv')
#show the pandastable application before you close the app, the process will be blocked
data_explore(df)
#use df after making change through the GUI
