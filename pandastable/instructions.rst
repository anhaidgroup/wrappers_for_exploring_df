## Dependencies
1. Python >= 2.7 or Python >= 3.3
2. Numpy
3. Matplotlib
4. Pandas



Installation: pip install pandastable, for python 3, pip3 install pandastable
Explore data: just type dataexplore in shell to open the GUI
Interact between the GUI and Python environment:
from exploredata import ExploreData
df = pandas.read_csv('filename')
We could open the Gui and pass the df to the Gui by typing
app = ExploreData(df)
After making changes though the GUI, we could directly access the changed data frame df. 


