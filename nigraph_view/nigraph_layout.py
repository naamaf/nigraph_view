# -*- coding: utf-8 -*-

"""Main module."""
import numpy as np 
import nigraph as ng

from bokeh.plotting import figure, curdoc
from bokeh.models import Button, CustomJS, Div
from bokeh.layouts import column, row, layout
from bokeh.models.ranges import Range1d
from bokeh.models.widgets import TextInput, Button, PreText, Dropdown, Slider
from functools import partial
from pathlib import Path

# genaral 
TOOLS = "wheel_zoom,box_zoom,reset"
total_width = 1200
data = ng.Scan()

# Header
header = PreText(text="Welcome to NiGraph_View", style={'font-size': '200%', 'color': 'blue'})
warning_win = PreText(text="Warning Window: No Warning for Now!")

# Choose map
def accept_map_path():
    # add validating function
    try:
        data.set_file(Path(map_path.value))
    except UserWarning as e:
        warning_win.text = str(e)

map_path = TextInput(value="", title="Map Path", width=int(total_width/4), height=50)
accept_map_button = Button(label="Accept Map Input", width=int(total_width/4), height=32, margin=[23,0,0,0])
accept_map_button.on_click(accept_map_path)

# Choose atlas and atlas metadata  
def accept_atlas_and_meta_path():
    try:
        data.set_atlas(Path(atlas_path.value), Path(metadata_path.value))
        
    except UserWarning as e:
        warning_win.text = str(e)
        

atlas_path = TextInput(value="", title="Atlas Path:", width=int(total_width/4), height=50)
metadata_path = TextInput(value="", title="Atlas Metadata Path:", width=int(total_width/4), height=50)
accept_atlas_and_meta_button = Button(label="Accept Atlas and Metadata Input", width=int(total_width/4), height=32, margin=[23,0,0,0])
accept_atlas_and_meta_button.on_click(accept_atlas_and_meta_path)

# Connectivity
def label_array(orig_list):
    x_labels = [[list(orig_list) for i in range(len(orig_list))]]
    revered_labels = orig_list[::-1]
    y_labels = [[[revered_labels[i]]*len(revered_labels) for i in range(len(revered_labels))]]
    return x_labels, y_labels

def get_conn_datasource():
    conn_mat = np.flip(data.connectivity_matrix, axis=0) # slipped so diagonal is top to bottom
    label_names = list(data.labels.area)
    label_numbers = list(data.labels.index) 
    x_names, y_names = label_array(label_names)
    x_numbers, y_numbers = label_array(label_numbers)
    
    source = ColumnDataSource(
    data = {
        "image" : [conn_mat],
        "x_names": x_names,
        "y_names": y_names,
        "x_numbers": x_numbers,
        "y_numbers": y_numbers,
        })
    return source

def plot_conn_mat():
    source = get_conn_datasource()
    conn_mat_fig.image("image", x = 0, y = 0, dw = 7, dh = 7, source = source)  
    conn_mat_fig.add_tools(HoverTool(tooltips =[("value:", "@image"), ("x parcel name", "@x_names"), ("y parcel name", "@y_names"), 
        ("x parcel number", "@x_numbers"), ("y parcel number", "@y_numbers")]))
    conn_mat_fig.xaxis.visible = False
    conn_mat_fig.yaxis.visible = False

conn_button = Button(label="Compute Connectivity Matrix", width=int(total_width/4)*3+15, height=60)
conn_button.on_click(plot_conn_mat)
conn_mat_fig = figure(tools=TOOLS, width=int(total_width/2), height=550) 

# Connectivity measures table
def connectivity_measure(text_name, label):
    text_name.text = str(data.measure(label))

cc_value = PreText(text=" ")
msp_value = PreText(text=" ")
dd_value = PreText(text=" ")
nc_value = PreText(text=" ")
ec_value = PreText(text=" ")
mcc_value = PreText(text=" ")

cc = Button(label="Closness Centrality", width=int(total_width/8))
cc.on_click(partial(connectivity_measure, text_name=cc_value, label=cc.label))
msp = Button(label="Mean Shortest Path", width=int(total_width/8))
msp.on_click(partial(connectivity_measure, text_name=msp_value, label=msp.label))
dd = Button(label="Degree Distribution", width=int(total_width/8))
dd.on_click(partial(connectivity_measure, text_name=dd_value, label=dd.label))
nc = Button(label="Node Connectivity", width=int(total_width/8))
nc.on_click(partial(connectivity_measure, text_name=nc_value, label=nc.label))
ec = Button(label="Edge Connectivity", width=int(total_width/8))
ec.on_click(partial(connectivity_measure, text_name=ec_value, label=ec.label))
mcc = Button(label="Mean Clustering", width=int(total_width/8))
mcc.on_click(partial(connectivity_measure, text_name=mcc_value, label=mcc.label))

# fMRI header
fMRIheader = PreText(text="For ROI analysis", style={'font-size': '200%', 'color': 'blue'})

# ROI stuff

# Choose ROI to use
def accept_ROI_path_and_prefix():
    try:
        data.set_roi(ROI_path.value, ROI_prefix.value)
    except UserWarning as e:
        warning_win.text = e
    
ROI_path = TextInput(value=" ", title="ROI Path", width=int(total_width/4), height=50)
ROI_prefix = TextInput(value=" ", title="ROI Prefix", width=int(total_width/4), height=50)

accept_ROI_button = Button(label="Accept ROI Inputs", width=int(total_width/4), height=32, margin=[23,0,0,0])
accept_ROI_button.on_click(accept_ROI_path_and_prefix)

# initiate ROI figure stiff
ROI_fig = figure(tools=TOOLS, width=int(total_width/2), height=550)
drop_menu = [("dim1", '0'), ("dim2", '1'), ("dim3", '2')]
choose_dim = Dropdown(label="choose dimension to slide", menu=drop_menu, value='0', width=int(total_width/2), height=50)
slider = Slider(start=0, end=100, step=1, value=40, width=int(total_width/2), height=50)

def remove_brain(old_brain):
    for glyph in old_brain:
        ROI_fig.renderers.remove(glyph)

def plot_ROI_fig():
    img = data.seed_based
    if img is None:
        warning_win.text = "Wrong File!"

    ROI_fig.image([img[slider.value, :, :].T], x=0, y=0, dw=(img.shape[1]/img.shape[2])*7, dh=7, palette="Greys256", name = 'brain')

    def update(attrname, old, new):
        dim = int(choose_dim.value)
        slider.end = img.shape[dim]
        current_slice = slider.value

        old_brain = ROI_fig.select('brain')
        remove_brain(old_brain)
            
        if dim == 0:
            ROI_fig.x_range = Range1d(0,img.shape[1])
            ROI_fig.y_range = Range1d(0,img.shape[2])
            ROI_fig.image([img[current_slice, :, :].T], x=0, y=0, dw=(img.shape[1]/img.shape[2])*7, dh=7, palette="Greys256",name = 'brain')
        elif dim == 1:
            ROI_fig.x_range = Range1d(0,img.shape[0])
            ROI_fig.y_range = Range1d(0,img.shape[2])
            ROI_fig.image([img[:, current_slice, :].T], x=0, y=0, dw=7, dh=7, palette="Greys256", name = 'brain')
        elif dim == 2:
            ROI_fig.x_range = Range1d(0,img.shape[0])
            ROI_fig.y_range = Range1d(0,img.shape[1])
            ROI_fig.image([img[:, :, current_slice].T], x=0, y=0, dw=7, dh=(img.shape[1]/img.shape[0])*7, palette="Greys256", name = 'brain')

    for w in [slider, choose_dim]:
        w.on_change("value",update)
        
plot_button_ROI_fig = Button(label="Plot ROI", width=int(total_width/4), height=32, margin=[23,0,0,0])
plot_button_ROI_fig.on_click(plot_ROI_fig)

#orgenize figures
curdoc().add_root(layout([
    [header],
    [warning_win],
    [map_path, accept_map_button], 
    [atlas_path, metadata_path, accept_atlas_and_meta_button],
    [conn_button],
    [conn_mat_fig, [[cc,cc_value],[msp,msp_value],[dd,dd_value],[nc,nc_value],[ec,ec_value],[mcc,mcc_value]]],
    [fMRIheader],
    [ROI_path, ROI_prefix, accept_ROI_button],
    [choose_dim],
    [ROI_fig],
    [slider],
]))

