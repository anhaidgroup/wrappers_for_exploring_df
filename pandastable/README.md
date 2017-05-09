# Installation instructions


## Requirements

Python >= 2.7 or Python >= 3.4

## Platforms

Tested on Windows with Python 3.4, 3.5, 3.6
numpy version: 1.11.3
matplotlib version: 2.0.0
pandas version: 0.19.2
pandastable version: 0.7.2

## Dependencies

1. numpy
2. matplotlib
3. pandas
4. pandastable


## Instructions to use this wrapper

1. First, install the dependencies using pip or conda.

		$pip install pandas table
	or

		$conda install conda install -c dmnfarrell pandastable=0.7.1
2. Next, import explore module from pandastable wrapper directory like this:

  		>>>from exploredata import ExploreData
  
3. Finally, explore the dataframe using ExploreData command like this:
  
  		>>>df = pandas.read_csv('file.csv')
  
  		>>>app = ExploreData(df)

The above command will open a GUI filled with 'df' contents. The user can 
explore/update the dataframe in the GUI and after exploration he/she can 
close the GUI. The updated dataframe can be accessed using 'df' variable
directly.



## Example IPython notebooks

For more examples, please refer to the IPython notebooks in the examples directory.

