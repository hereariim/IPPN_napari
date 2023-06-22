# Exercise

## 1- `_widget.py`

We're going to design two widgets:

- A widget for thresholding

- A widget to calculate leaf area

So, for each widget, we're going to create a function to contain the script and a GUI.

### Widget for thresholding

We have two input:
- image in array
- name of filter

In napari, **image** input is presented as `napari.types` object.

In magicgui, we introduce two variables:
- `selected_image`: current image in napari window which is given by `ImageData` object from `napari.types`.
- `filter_selected`: current selected thresholding which is given by user.

⚠️Don't forget to import `ImageData` and `LabelsData` in `_widget.py`: `from napari.types import ImageData, LabelsData`

```
from napari.types import ImageData, LabelsData

@magic_factory(call_button="Run", filter_selected={"choices": ['otsu', 'li']})
def threshold_f(selected_image: ImageData,filter_selected='otsu') -> LabelsData:
    ###
    SCRIPT
    ###
    return mask
```

More information about [napari.types](https://napari.org/stable/api/napari.types.html)

### Widget to calculate leaf area

We have one input:
- mask in layer

In magicgui, we introduce a single variable:
- `result_widget`: Bool variable to display a LineEdit widget the output of the function.

Here `masks` is a layer labels in napari window. We need the data of `masks`. So we use the attribute `masks.data` to get data of mask.

```
@magic_factory(result_widget=True)
def leaf_area(masks: "napari.layers.Labels"):
    mask = masks.data
    ###
    SCRIPT
    ###
    return labels_leaf_area
```
More information about [napari.layers.Labels](https://napari.org/stable/api/napari.layers.Labels.html)

*See correction: `_widget.py`*

## 2- `napari.yaml`

In contributions section, we add our widget functions:
```
  - id: napari-thresholds.my_widget #must be unique !
    title: Thresholds
    python_name: napari_thresholds._widget:threshold_f

  - id: napari-thresholds.my_leaf_area #must be unique !
    python_name: napari_thresholds._widget:leaf_area
    title: Leaf area
```
Here, we identify in backend our widget as
```
napari-thresholds.my_widget
```
In widgets section, we add some information to display our widget:
```
  - command: napari-thresholds.my_widget #identity backend
    display_name: Thresholds
  - command: napari-thresholds.my_leaf_area #identity backend
    display_name: Leaf area
```

*See correction: `napari.yaml`*

## 3- `__init__.py`
To be rigorous, we add our function to the plugin's family of functions
```
__version__ = "0.0.1"
from ._widget import ExampleQWidget, example_magic_widget, threshold_f, leaf_area

__all__ = (
    "ExampleQWidget",
    "example_magic_widget",
    "threshold_f",
    "leaf_area",
)
```

*See correction: `__init__.py`*

## 4-  `setup.cfg`
In the configuration file, we specify the libraries we will use in the script to threshold an image. In `[options]` section, we add in `install_requires` variable our used libraries such as `scikit-image`
```
install_requires =
    numpy
    magicgui
    qtpy
    scikit-image
    napari
```

*See correction: `setup.cfg`*

## 5-  `test_widget.py`

When the plugin is working well, you can add a few tests to each widget to see if the widgets work when a modification has been made to the code. These tests indicate that the plugin is working properly.

Here, we add test for each widget.

### Threshold
Let's suppose a user changes our code.
We add test to check if output is a numpy array and binary

```
import pytest
from napari.types import ImageData, LabelsData
from napari.layers import Image, Labels

# We create a RGB image randomly
@pytest.fixture
def im_rgb():
    return ImageData(np.random.randint(256,size=(256,256,3)))

# We establish our function by highlighting the arguments and argument keys (arg of magicgui)
def get_er(*args, **kwargs):
    er_func = threshold_f()
    return er_func(*args, **kwargs)

# We run a test to check if output is numpy array and binary
def test_threshold(im_rgb):
    my_widget_thd = get_er(im_rgb,filter_selected='otsu')
    #check if output is numpy array
    assert type(my_widget_thd)==np.ndarray
    #check if output is binary
    assert len(np.unique(my_widget_thd))==2
```

### Leaf Area
Let's suppose a user changes our code.
We add test to check if leaf area is integer and positive

```
# We create a binary mask randomly
@pytest.fixture
def mask_bin():
    return Labels(np.random.randint(2,size=(256,256,1)))

# We establish our function by highlighting the arguments and argument keys (arg of magicgui)
def get_ed(*args, **kwargs):
    ed_func = leaf_area()
    return ed_func(*args, **kwargs)

# We run a test to check if output of widget is integer and positive
def test_leaf_area(mask_bin):
    my_widget_lf_area = get_ed(mask_bin)
    # check if output is integer
    assert isinstance(my_widget_lf_area,int)
```

*See correction: `test_widget.py`*

## 6-  `README.md`

You should add some relevant information to inform user about your plugin and how to use it.

*See correction: `README.md`*
