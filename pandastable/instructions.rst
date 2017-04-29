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
1. Numpy
2. Matplotlib
3. Pandas
4. Pandastable


Instructions to use this wrapper
---------------------------------
1. First, install the dependencies using pip or conda.
2. Next, import explore module from pandastable wrapper directory like this:

  from exploredata import ExploreData
  
3. Finally, explore the dataframe using ExploreData command like this:
  
  df = pandas.read_csv('file.csv')
  
  app = ExploreData(df)

The above command will open a GUI filled with 'df' contents. The user can 
explore/update the dataframe in the GUI and after exploration he/she can 
close the GUI. The updated dataframe can be accessed using 'df' variable
directly.

Example usage
-------------


Example IPython notebooks
--------------------------
For more examples, please refer to the IPython notebooks in the examples directory.

