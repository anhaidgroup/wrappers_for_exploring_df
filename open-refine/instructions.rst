Installation instructions
-------------------------

Requirements
------------
Python >= 2.7 or Python >= 3.4

Platforms
---------
Tested on Windows 10 with Python 2.7, 3.5.

Dependencies
------------
1. Requests
2. Urllib
3. Open Refine


Instructions to use this wrapper
---------------------------------
1. First, you should install Openrefine. About that, you could refer to this link for the installation of different OS:  https://github.com/OpenRefine/OpenRefine/wiki/Installation-Instructions

2. Then you need to execute the Open Refine application, i.e. having the Open Refine server running.

3. Next, create your project under the openrefine wrapper directory, and then import explore module like this:

  from refine import Refine
  
4. Finally, explore the dataframe using Refine command like this:
  
  df = pandas.read_csv("filename")
  
  p = Refine(df)

  newdf = p.export_pandas_frame()

The above command will open Open Refine GUI filled with 'df' contents. The user can 
explore/update the dataframe in the GUI and after exploration he/she can 
close the GUI. The updated dataframe can be accessed using this function: newdf = p.export_pandas_frame()
After calling p.export_pandas_frame(), the open refine project will be deleted at the same time. If you want to
explore the data, you should call p = Refine(df) to create a new open refine project. 

Example usage
-------------


Example IPython notebooks
--------------------------
For more examples, please refer to the IPython notebooks in the examples directory.

