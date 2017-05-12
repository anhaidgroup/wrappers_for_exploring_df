#Initial import
from open_refine_wrapper import data_explore
import pandas as pd

#read in pandas dataframe
df = pd.read_csv('example_input_table.csv')

#Invoke the open refine gui for data exploration
p = data_explore(df,"http://127.0.0.1:3333/")

#Save the project back to our dataframe
# after calling export_pandas_frame, the openRefine project will be deleted automatically
df = p.export_pandas_frame()
