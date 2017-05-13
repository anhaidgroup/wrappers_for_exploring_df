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

3. Next, Clone this repository to a temporary directory in your local machine.

4. Next, go to the directory which includes the file to explore and open a Python shell or IPython notebook. 

5. Then, include the path of the temporary directory (from step 3) to system's path like this:

        >>> import sys
        >>> sys.path.append('path/to/this/repository')

2. Next, import explore module from pandastable wrapper directory like this:

  		>>>from pandastable.pandastable_wrapper import explore_data
  
3. Finally, explore the dataframe using data_explore_data command like this:
  
  		>>>df = pandas.read_csv('file.csv')
  
  		>>>data_explore(df)


The above command will open a GUI filled with 'df' contents as shown below:
![ScreenShot](https://raw.github.com/anhaidgroup/wrappers_for_exploring_df/master/pandastable/figures/Screenshot_PandasTable.png)

The user can explore/update the dataframe in the GUI and after exploration he/she can 
close the GUI. The updated dataframe can be accessed using the variable assigned to 
the dataframe (for example: 'df' in the above command).



## Example IPython notebooks

For more examples, please refer to the IPython notebooks in the examples directory.

