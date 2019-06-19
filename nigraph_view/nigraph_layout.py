# -*- coding: utf-8 -*-

"""Main module."""
from bokeh.plotting import figure, curdoc
from bokeh.models import Button, CustomJS
from bokeh.layouts import column, row, layout
from bokeh.models.ranges import Range1d
from bokeh.models.widgets import TextInput, Button, Select, CheckboxGroup, DataTable, DateFormatter, TableColumn, PreText

# genaral 
TOOLS = "wheel_zoom,box_zoom,reset"

total_width = 1200

# Header
header = PreText(text="Welcome to NyGraph_View")
warning = PreText(text="No Warnings for now!")

# Choose file button
def ChooseFileButton():
    pass

fileButton = TextInput(value="Enter File Path", title="Choose File", width=int(total_width/4), height=50)

# OK button
def approveFile():
    pass

approveFileButton = Button(label="Approve File", width=int(total_width/4), height=32, margin=[23,0,0,0])
approveFileButton.on_click(approveFile)


# Choose atlas button
def ChooseAtlasButton():
    pass

AtlasButton = TextInput(value=" ", title="Choose Atlas", width=int(total_width/4), height=50)

# Choose metadata button
def ChooseMetadataButton():
    pass

MetadataButton = TextInput(value=" ", title="Choose MetaData", width=int(total_width/4), height=50)

# Approve Atlas
def approveAtlas():
    pass

approveAtlasButton = Button(label="Approve Atlas and Metadata", width=int(total_width/4), height=32, margin=[23,0,0,0])
approveAtlasButton.on_click(approveAtlas)


# Compute connectivity button
def ComputeConnectivityButton():
    pass

ConnectivityButton = Button(label="Compute Connectivity", width=int(total_width/4)*3+15, height=60)
ConnectivityButton.on_click(ComputeConnectivityButton)

# Connectivity matrix figure
connectivityMatrix = figure(tools=TOOLS, x_range=(0,100), y_range=(0,100), width=int(total_width/2), height=550) 

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
fMRIheader = PreText(text="For ROI analysis")

# Image view figure
imageView = figure(tools=TOOLS, x_range=(0,100), y_range=(0,100), width=int(total_width/2), height=550) 

# Slice direction dropdown
def sliceDropdown():
    pass

sliceDropdownMenu = Select(title="For fMRI Connectivity Only: Choose Direction:", value="X", options=["X", "Y", "Z"], width=int(total_width/2), height=50)

def ChooseROIButton():
    pass

roiButton = TextInput(value=" ", title="Choose ROI", width=int(total_width/4), height=50)

# OK button
def approveROI():
    pass

approveROIButton = Button(label="Approve ROI", width=int(total_width/4), height=32, margin=[23,0,0,0])
approveROIButton.on_click(approveROI)

#orgenize figures
curdoc().add_root(layout([
    [header],
    [warning],
    [fileButton, approveFileButton], 
    [AtlasButton, MetadataButton, approveAtlasButton],
    [ConnectivityButton],
    [connectivityMatrix, [[cc,cc_value],[msp,msp_value],[dd,dd_value],[nc,nc_value],[ec,ec_value]]],
    [fMRIheader],
    [roiButton, approveROIButton],
    [sliceDropdownMenu],
    [imageView],
]))
