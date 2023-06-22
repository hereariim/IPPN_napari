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

In magicgui, we introduce two variables:
- `selected_image`: current image in napari window which is given by `ImageData` object from `napari.types`.
- `filter_selected`: current selected thresholding which is given by user.

⚠️Don't forget to import `ImageData` and `LabelsData` in `_widget.py`: `from napari.types import ImageData, LabelsData`

```
@magic_factory(call_button="Run", filter_selected={"choices": ['otsu', 'li']})
def threshold_f(selected_image: ImageData,filter_selected='otsu') -> LabelsData:
    ###
    SCRIPT
    ###
    return mask
```

### Widget for thresholding

We have one input:
- mask in layer

In magicgui, we introduce a single variable:
- `result_widget`: Bool variable to display a LineEdit widget the output of the function.

```
@magic_factory(result_widget=True)
def leaf_area(mask: "napari.layers.Labels"):
    ###
    SCRIPT
    ###
    return labels_leaf_area
```

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

*See correction:*

## 6-  `README.md`

You should add some relevant information to inform user about your plugin and how to use it.

*See correction: `README.md`*