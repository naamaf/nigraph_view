# -*- coding: utf-8 -*-

"""Main module."""
from bokeh.plotting import figure, curdoc
from bokeh.models import Button, CustomJS, HoverTool, ColumnDataSource
from bokeh.layouts import column, row, layout
from bokeh.models.ranges import Range1d
from bokeh.models.widgets import TextInput, Button, Select
from tkinter import filedialog, Tk
import numpy as np 


# genaral 
TOOLS = "wheel_zoom,box_zoom,reset,hover"
total_width = 1000


def accept_map_button():
    # add validating function
    data.set_path(map_path.value)


def accept_atlas_and_meta_button():
    # add validating function
    data.set_atlas(atlas_path.value, metadata_path.value)


# Compute connectivity 

def plot_conn_mat():
    flipped_mat = np.flip(data.connectivity_matrix, axis=0)
    label_names = list(data.labels.area)
    reverse_names = label_names[::-1]

    # maybe use later the numbers
    # label_numbers = list(data.labels.index) 
    # reverse_numbers = label_numbers[::-1]

    conn_mat_fig.image(image = [flipped_mat], x = 0, y = 0, dw = 7, dh = 7)  

    # add labels to axes and place them in the middle of each box
    ticks = [i+0.5 for i in range(len(label_names))]

    x_label_dict = {i+0.5:label_names[i] for i in range(len(label_names))}
    conn_mat_fig.xaxis.ticker = ticks
    conn_mat_fig.xaxis.major_label_overrides = x_label_dict
    conn_mat_fig.xaxis.major_label_orientation = np.pi/4

    y_label_dict = {i+0.5:reverse_names[i] for i in range(len(label_names))}
    conn_mat_fig.yaxis.ticker = ticks
    conn_mat_fig.yaxis.major_label_overrides = y_label_dict

    # currently not possible...
    # hover = conn_mat_fig.select(dict(type=HoverTool))
    # hover.tooltips =[("x label name", "@names_x"), ("y label name", "@names_y"), ("x label number", "@numbers_x"), ("y label number", "@numbers_y")]
    # hover.mode = 'mouse'

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
