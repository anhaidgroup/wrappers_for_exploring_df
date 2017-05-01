Installation instructions
-------------------------

Requirements
------------
Python >= 2.7 or Python >= 3.3

Platforms
---------
Tested on ..

Dependencies
------------
1. Requests
2. Urllib
3. Open Refine


Instructions to use this wrapper
---------------------------------
1. First, for the different platform, we could refer to this link:  https://github.com/OpenRefine/OpenRefine/wiki/Installation-Instructions, for linux, we could just download the code. 

2. Next, import explore module from pandastable wrapper directory like this:

  from refine import Refine
  
3. Finally, explore the dataframe using ExploreData command like this:
  
  df = pandas.read_csv("filename")
  
  p = Refine(df)

  newdf = p.export_pandas_frame()

The above command will open Open Refine GUI filled with 'df' contents. The user can 
explore/update the dataframe in the GUI and after exploration he/she can 
close the GUI. The updated dataframe can be accessed using this function: newdf = p.export_pandas_frame()

Example usage
-------------


Example IPython notebooks
--------------------------
For more examples, please refer to the IPython notebooks in the examples directory.

