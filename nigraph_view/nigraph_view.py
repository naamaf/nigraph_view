# -*- coding: utf-8 -*-

"""Main module."""
from bokeh.plotting import figure, curdoc
from bokeh.models import Button, CustomJS
from bokeh.layouts import column, row, layout
from bokeh.models.ranges import Range1d
from bokeh.models.widgets import TextInput, Button, Select

# genaral 
TOOLS = "wheel_zoom,box_zoom,reset"

total_width = 1000

# Choose file button
def ChooseFileButton():
    pass

fileButton = Button(label="Choose Map", width=int(total_width/6), height=30)
fileButton.on_click(ChooseFileButton)

# Map name text box
def mapNameTextbox():
    pass

mapName = TextInput(value="default", title="Map Name", width=int(total_width/6), height=50)

# Choose atlas button
def ChooseAtlasButton():
    pass

AtlasButton = Button(label="Choose Atlas", width=int(total_width/6), height=30)
AtlasButton.on_click(ChooseAtlasButton)

# Choose metadata button
def ChooseMetadataButton():
    pass

MetadataButton = Button(label="Choose MetaData", width=int(total_width/6), height=30)
MetadataButton.on_click(ChooseMetadataButton)

# Atlas name text box
def atlasNameTextbox():
    pass

atlasName = TextInput(value="default", title="Atlas Name", width=int(total_width/6), height=50)

# Compute connectivity button
def ComputeConnectivityButton():
    pass

ConnectivityButton = Button(label="Compute Connectivity", width=int(total_width/6), height=30)
ConnectivityButton.on_click(ComputeConnectivityButton)

# Connectivity matrix figure
connectivityMatrix = figure(tools=TOOLS, x_range=(0,100), y_range=(0,100), width=int(total_width/2)+30, height=530) 

# Compute connectivity measure dropdown
def ComputeConnectivityMeasure():
    pass

connectivityDropdown = Select(title="Choose Connectivity Measure to Compute:", value="X", options=["X", "Y", "Z"], width=int(total_width/4), height=50)

# Compute connectivity measure textbox
def connectivityMeasureTextbox():
    pass

connectivityMeasure = TextInput(value="default", title="Connectivity Measure", width=int(total_width/4), height=50)

# Image view figure
imageView = figure(tools=TOOLS, x_range=(0,100), y_range=(0,100), width=450, height=450) 


# Slice direction dropdown
def sliceDropdown():
    pass

sliceDropdownMenu = Select(title="For fMRI Connectivity Only: Choose Direction:", value="X", options=["X", "Y", "Z"], width=int(total_width/6), height=50)

# Add ROI button
def addroiButton():
    pass

roiButton = Button(label="Add ROI", width=int(total_width/6), height=30)
roiButton.on_click(addroiButton)

# ROI name textbox
def roiNameTextbox():
    pass

roiName = TextInput(value="default", title="ROI Name", width=int(total_width/6), height=50)

# Choose ROI dropdown
def roiDropdown():
    pass

roiDropdownMenu = Select(title="Choose ROI:", value="X", options=["X", "Y", "Z"], width=int(total_width/6), height=50)

#orgenize figures
curdoc().add_root(layout([
    [fileButton, mapName, ConnectivityButton, AtlasButton, atlasName,MetadataButton],
    [connectivityMatrix, [sliceDropdownMenu, imageView]],
    [connectivityDropdown, connectivityMeasure, roiButton, roiName, roiDropdownMenu],
], sizing_mode="fixed"))
