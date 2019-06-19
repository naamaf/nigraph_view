# -*- coding: utf-8 -*-

"""Main module."""
from bokeh.plotting import figure, curdoc
from bokeh.models import Button, CustomJS
from bokeh.layouts import column, row, layout
from bokeh.models.ranges import Range1d
from bokeh.models.widgets import TextInput, Button, Select, CheckboxGroup, DataTable, DateFormatter, TableColumn, PreText
import nigraph_view as ng_v

# genaral 
TOOLS = "wheel_zoom,box_zoom,reset"
total_width = 1200
data = Scan()

# Header
header = PreText(text="Welcome to NyGraph_View", style={'font-size': '200%', 'color': 'blue'})
warning = PreText(text="Warning Window: No Warning for Now!")

# Choose map
map_path = TextInput(value=" ", title="Map Path", width=int(total_width/4), height=50)
accept_map_path = Button(label="Accept Map Input", width=int(total_width/4), height=32, margin=[23,0,0,0])
accept_map_path.on_click(ng_v.accept_map_button)

# Choose atlas and atlas metadata  
atlas_path = TextInput(value=" ", title="Atlas Path:", width=int(total_width/4), height=50)
metadata_path = TextInput(value=" ", title="Atlas Metadata Path:", width=int(total_width/4), height=50)
accept_atlas_and_meta_path = Button(label="Accept Atlas and Metadata Input", width=int(total_width/4), height=32, margin=[23,0,0,0])
accept_atlas_and_meta_path.on_click(ng_v.accept_atlas_and_meta_button)



# Connectivity
conn_button = Button(label="Compute Connectivity Matrix", width=int(total_width/4)*3+15, height=60)
conn_button.on_click(np_v.plot_conn_mat)
conn_mat_fig = figure(tools=TOOLS, width=int(total_width/2), height=550) 

# Connectivity measures table
def measure(label):
    return label
def ComputeConnectivityMeasureCC():
    cc_value.text=str(measure(cc.label))
def ComputeConnectivityMeasureMSP():
    msp_value.text=str(measure(msp.label))
def ComputeConnectivityMeasureDD():
    dd_value.text=str(measure(dd.label))
def ComputeConnectivityMeasureNC():
    nc_value.text=str(measure(nc.label))
def ComputeConnectivityMeasureEC():
    ec_value.text=str(measure(ec.label))

cc_value = PreText(text="A")
msp_value = PreText(text="B")
dd_value = PreText(text="C")
nc_value = PreText(text="D")
ec_value = PreText(text="E")

# Compute connectivity measure dropdown
cc = Button(label="closness centrality", width=int(total_width/8))
cc.on_click(ComputeConnectivityMeasureCC)
msp = Button(label="mean shortest path", width=int(total_width/8))
msp.on_click(ComputeConnectivityMeasureMSP)
dd = Button(label="degree distribution", width=int(total_width/8))
dd.on_click(ComputeConnectivityMeasureDD)
nc = Button(label="node connectivity", width=int(total_width/8))
nc.on_click(ComputeConnectivityMeasureNC)
ec = Button(label="edge connectivity", width=int(total_width/8))
ec.on_click(ComputeConnectivityMeasureEC)

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
    [conn_mat_fig, [[cc,cc_value],[msp,msp_value],[dd,dd_value],[nc,nc_value],[ec,ec_value]]],
    [fMRIheader],
    [roiButton, approveROIButton],
    [sliceDropdownMenu],
    [imageView],
]))
