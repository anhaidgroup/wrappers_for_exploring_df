#Initial import
from pandastable_wrapper import data_explore
import pandas as pd

#read in pandas dataframe
df = pd.read_csv("example_input_table.csv")

#Invoke the pandastable gui for data exploration
#The process will be blocked until closing the GUI
data_explore(df)

#use df after making change through the GUI
