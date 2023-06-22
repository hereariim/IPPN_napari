import numpy as np

from napari_thresholds import ExampleQWidget, example_magic_widget, threshold_f, leaf_area

import pytest
from napari.types import ImageData, LabelsData
from napari.layers import Image, Labels

# make_napari_viewer is a pytest fixture that returns a napari viewer object
# capsys is a pytest fixture that captures stdout and stderr output streams
def test_example_q_widget(make_napari_viewer, capsys):
    # make viewer and add an image layer using our fixture
    viewer = make_napari_viewer()
    viewer.add_image(np.random.random((100, 100)))

    # create our widget, passing in the viewer
    my_widget = ExampleQWidget(viewer)

    # call our widget method
    my_widget._on_click()

    # read captured output and check that it's as we expected
    captured = capsys.readouterr()
    assert captured.out == "napari has 1 layers\n"


def test_example_magic_widget(make_napari_viewer, capsys):
    viewer = make_napari_viewer()
    layer = viewer.add_image(np.random.random((100, 100)))

    # this time, our widget will be a MagicFactory or FunctionGui instance
    my_widget = example_magic_widget()

    # if we "call" this object, it'll execute our function
    my_widget(viewer.layers[0])

    # read captured output and check that it's as we expected
    captured = capsys.readouterr()
    assert captured.out == f"you have selected {layer}\n"

@pytest.fixture
def im_rgb():
    return ImageData(np.random.randint(256,size=(256,256,3)))

@pytest.fixture
def mask_bin():
    return Labels(np.random.randint(2,size=(256,256,1)))

def get_er(*args, **kwargs):
    er_func = threshold_f()
    return er_func(*args, **kwargs)

def test_threshold(im_rgb):
    my_widget_thd = get_er(im_rgb,filter_selected='otsu')
    #check if output is numpy array
    assert type(my_widget_thd)==np.ndarray
    #check if output is binary
    assert len(np.unique(my_widget_thd))==2

def get_ed(*args, **kwargs):
    ed_func = leaf_area()
    return ed_func(*args, **kwargs)
    
def test_leaf_area(mask_bin):
    my_widget_lf_area = get_ed(mask_bin)
    #check if output is numpy array
    assert isinstance(my_widget_lf_area,int)
    assert my_widget_lf_area > 0
