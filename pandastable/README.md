# Installation instructions


## Requirements

Python >= 3.4

## Platforms tested

Windows 10, Ubuntu 15.04

## Dependencies

1. numpy
2. matplotlib
3. pandas
4. pandastable


## Instructions to use this wrapper

1. First, install the dependencies using pip or conda.

		$pip install pandastable
	or

		$conda install conda install -c dmnfarrell pandastable=0.7.1
2. Next, import explore module from pandastable wrapper directory like this:

  		>>>from pandastable.pandastable_wrapper import explore_data
  
3. Finally, explore the dataframe using explore_data command like this:
  
  		>>>df = pandas.read_csv('file.csv')
  
  		>>>app = explore_data(df)
		
		>>>app.mainloop()

The above command will open a GUI filled with 'df' contents as shown below:



The user can explore/update the dataframe in the GUI and after exploration he/she can 
close the GUI. The updated dataframe can be accessed using the variable assigned to 
the dataframe (for example: 'df' in the above command).



## Example IPython notebooks

For more examples, please refer to the IPython notebooks in the examples directory.

