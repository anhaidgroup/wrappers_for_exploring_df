Requirement: Requires python>=3.3 or 2.7 and numpy, matplotlib and pandas.
Installation: pip install pandastable, for python 3, pip3 install pandastable
Explore data: just type dataexplore in shell to open the GUI
Interact between the GUI and Python environment:
from exploredata import ExploreData
df = pandas.read_csv('filename')
We could open the Gui and pass the df to the Gui by typing
app = ExploreData(df)
After making changes though the GUI, we could directly access the changed data frame df. 


