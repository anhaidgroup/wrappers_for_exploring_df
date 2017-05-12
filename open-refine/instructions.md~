# Installation instructions

## Requirements

Python >= 2.7 or Python >= 3.4

## Platforms

######## Update this as per pandastable template

## Dependencies

1. requests
2. urllib
3. OpenRefine


## Instructions to use this wrapper

1. First, you should install OpenRefine. To install OpenRefine, go to this [link]( https://github.com/OpenRefine/OpenRefine/wiki/Installation-Instructions) and follow the instructions for different platforms.

2. Then you need to execute the OpenRefine application. Specifically, go to this [link]( https://github.com/OpenRefine/OpenRefine/wiki/Installation-Instructions) and follow the instructions to run on different platforms. Once the OpenRefine starts, you will see something like this.

![ScreenShot](https://raw.github.com/anhaidgroup/wrappers_for_exploring_df/master/open-refine/figures/OpenRefineMain.PNG)

3. Next, Clone this repository to a temporary directory in your local machine.

4. Next, go to the directory which includes the file to explore and open a Python shell or IPython notebook. 

5. Then, include the path of the temporary directory (from step 3) to system's path like this:

        >>> import sys
        >>> sys.path.append('path/to/this/repository')
        
6. Next, import open refine wrapper like this 

        >>> from open-refine.open_refine_wrapper import data_explore
 
7. Next, copy the URL from the address bar of Open Refine browser (typically this will be http://127.0.0.1:3333) and explore the dataframe using data_explore command like this:
  
        >>>df = pandas.read_csv("example_input_table.csv")
  
        >>>p = data_explore(df, "http://127.0.0.1:3333") # replace http://127.0.0.1:3333 with approproate URL that you copied
  
  This is something you should expect to see
![ScreenShot](https://raw.github.com/anhaidgroup/wrappers_for_exploring_df/master/open-refine/figures/OpenRefinProject.PNG)
  

8. Finally, once the data exploration is done, you can simply close the window and the updated dataframe can be accessed like this:

        >>>df = p.export_pandas_frame()

## Example IPython notebooks

For more examples, please refer to the IPython notebooks in the examples directory.

