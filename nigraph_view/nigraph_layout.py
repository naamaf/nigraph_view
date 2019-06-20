# -*- coding: utf-8 -*-

"""Main module."""
import numpy as np 
import nigraph as ng

from bokeh.plotting import figure, curdoc
from bokeh.models import Button, CustomJS
from bokeh.layouts import column, row, layout
from bokeh.models.ranges import Range1d
from bokeh.models.widgets import TextInput, Button, PreText, Dropdown, Slider

# genaral 
TOOLS = "wheel_zoom,box_zoom,reset"
total_width = 1200
data = ng.Scan()

# Header
header = PreText(text="Welcome to NyGraph_View", style={'font-size': '200%', 'color': 'blue'})
warning = PreText(text="Warning Window: No Warning for Now!")

# Choose map
def accept_map_button():
    # add validating function
    data.set_file(map_path.value)

map_path = TextInput(value=" ", title="Map Path", width=int(total_width/4), height=50)
accept_map_path = Button(label="Accept Map Input", width=int(total_width/4), height=32, margin=[23,0,0,0])
accept_map_path.on_click(accept_map_button)

# Choose atlas and atlas metadata  
def accept_atlas_and_meta_button():
    # add validating function
    data.set_atlas(atlas_path.value, metadata_path.value)

atlas_path = TextInput(value=" ", title="Atlas Path:", width=int(total_width/4), height=50)
metadata_path = TextInput(value=" ", title="Atlas Metadata Path:", width=int(total_width/4), height=50)
accept_atlas_and_meta_path = Button(label="Accept Atlas and Metadata Input", width=int(total_width/4), height=32, margin=[23,0,0,0])
accept_atlas_and_meta_path.on_click(accept_atlas_and_meta_button)

# Connectivity
def name_array(names):
    x_labels = [list(names) for i in range(len(names))]
    y_labels = x_labels[::-1]
    return x_labels, y_labels

def plot_conn_mat():
    #flipped_mat = np.identity(3) #np.corrcoef(np.random.randint(10, size=(5,10))) ##np.flip(data.connectivity_matrix, axis=0)
    #label_names = ['a','b','c','d','e']  #list(data.labels.area)
    #reverse_names = label_names[::-1]

    location_source = ColumnDataSource(
        data = {
            "image" : [flipped_mat],
            "label_names": [],
            "reverse_names": []
            "label_numbers": list(data.labels.index)
            "reverse_numbers": label_numbers[::-1]
            })
        [data["label_names"], data["reverse_names"] = name_array(labels)

    # maybe use later the numbers
    # label_numbers = list(data.labels.index) 
    # reverse_numbers = label_numbers[::-1]

    conn_mat_fig.image("image", x = 0, y = 0, dw = 7, dh = 7, source = location_source)  

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
    conn_mat_fig.add_tools(HoverTool(tooltips =[("value:", "@image"), ("x", "@label_names"), ("y", "@reverse_names"), ("x_num", "@label_numbers"), ("y_num", "reverse_names"]))

conn_button = Button(label="Compute Connectivity Matrix", width=int(total_width/4)*3+15, height=60)
conn_button.on_click(plot_conn_mat)
conn_mat_fig = figure(tools=TOOLS, width=int(total_width/2), height=550) 

# Connectivity measures table
def ComputeConnectivityMeasureCC():
    cc_value.text=str(data.measure(cc.label))
def ComputeConnectivityMeasureMSP():
    msp_value.text=str(data.measure(msp.label))
def ComputeConnectivityMeasureDD():
    dd_value.text=str(data.measure(dd.label))
def ComputeConnectivityMeasureNC():
    nc_value.text=str(data.measure(nc.label))
def ComputeConnectivityMeasureEC():
    ec_value.text=str(data.measure(ec.label))
def ComputeConnectivityMeasureMCC():
    mcc_value.text=str(data.measure(mcc.label))

cc_value = PreText(text=" ")
msp_value = PreText(text=" ")
dd_value = PreText(text=" ")
nc_value = PreText(text=" ")
ec_value = PreText(text=" ")
mcc_value = PreText(text=" ")

# Compute connectivity measure dropdown
#cc = Button(label="Closness Centrality", width=int(total_width/8))
#cc.on_click(ComputeConnectivityMeasureCC)
#msp = Button(label="Mean Shortest Path", width=int(total_width/8))
#msp.on_click(ComputeConnectivityMeasureMSP)
#dd = Button(label="Degree Distribution", width=int(total_width/8))
#dd.on_click(ComputeConnectivityMeasureDD)
#nc = Button(label="Node Connectivity", width=int(total_width/8))
#nc.on_click(ComputeConnectivityMeasureNC)
#ec = Button(label="Edge Connectivity", width=int(total_width/8))
#ec.on_click(ComputeConnectivityMeasureEC)
for name, func in [
    ["Closness Centrality", ComputeConnectivityMeasureCC],
    ["Mean Shortest Path", ComputeConnectivityMeasureMSP],
    ["Degree Distribution", ComputeConnectivityMeasureDD],
    ["Node Connectivity", ComputeConnectivityMeasureNC],
    ["Edge Connectivity", ComputeConnectivityMeasureEC],
    ["Mean Clustering", ComputeConnectivityMeasureMCC]
]:
cc = Button(label=name[0], width=int(total_width/8))
cc.on_click(func[0])
msp = Button(label=name[1], width=int(total_width/8))
msp.on_click(func[1])
dd = Button(label=name[2], width=int(total_width/8))
dd.on_click(func[2])
nc = Button(label=name[3], width=int(total_width/8))
nc.on_click(func[3])
ec = Button(label=name[4], width=int(total_width/8))
ec.on_click(func[4])
mcc = Button(label=name[5], width=int(total_width/8))
mcc.on_click(func[5])

# fMRI header
fMRIheader = PreText(text="For ROI analysis", style={'font-size': '200%', 'color': 'blue'})

# Image view figure
imageView = figure(tools=TOOLS, x_range=(0,100), y_range=(0,100), width=int(total_width/2), height=550) 

# Slice direction dropdown

sliceDropdownMenu = Select(title="For fMRI Connectivity Only: Choose Direction:", value="X", options=["X", "Y", "Z"], width=int(total_width/2), height=50)


roiButton = TextInput(value=" ", title="Choose ROI", width=int(total_width/4), height=50)

# OK button

approveROIButton = Button(label="Approve ROI", width=int(total_width/4), height=32, margin=[23,0,0,0])
approveROIButton.on_click(approveROI)

#orgenize figures
curdoc().add_root(layout([
    [header],
    [warning],
    [map_path, accept_map_path], 
    [atlas_path, metadata_path, accept_atlas_and_meta_path],
    [conn_button],
    [conn_mat_fig, [[cc,cc_value],[msp,msp_value],[dd,dd_value],[nc,nc_value],[ec,ec_value],[mcc,mcc_value]]],
    [fMRIheader],
    [roiButton, approveROIButton],
    [sliceDropdownMenu],
    [imageView],
]))
