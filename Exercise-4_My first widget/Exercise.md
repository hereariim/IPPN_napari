# Exercise

## 1- `_widget.py`

We're going to create a function to contain the script and a GUI for the widget.

We have two input:
- image in array
- name of filter

In magicgui, we introduce two variables:
- `selected_image`: current image in napari window which is given by `ImageData` object from `napari.types`.

⚠️Don't forget to import `ImageData` in `_widget.py`: `from napari.types import ImageData`
```
@magic_factory(call_button="Run", filter_selected={"choices": ['otsu', 'li']})
def threshold_f(selected_image: ImageData,filter_selected='otsu') -> LabelsData:
    ###
    SCRIPT
    ###
    return mask
```

*See correction: `_widget.py`*

## 2- `napari.yaml`

In contributions section, we add our widget function:
```
  - id: napari-thresholds.my_widget #must be unique !
    title: Thresholds
    python_name: napari_thresholds._widget:threshold_f
```
Here, we identify in backend our widget as
```
napari-thresholds.my_widget
```
In widgets section, we add some information to display our widget:
```
  - command: napari-thresholds.my_widget #identity backend
    display_name: Thresholds
```

*See correction: `napari.yaml`*

## 3- `__init__.py`
To be rigorous, we add our function to the plugin's family of functions
```
from ._widget import ExampleQWidget, example_magic_widget, threshold_f

__all__ = (
    "ExampleQWidget",
    "example_magic_widget",
    "threshold_f",
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

## 7- Install your plugin in current environment

VII- When it's over, install plugin **in your computer** with in `napari-thresholds` directory where `pyproject.toml` is located

```
pip install -e .
```

⚠️ *Note: You install plugin in napari as python package. This command will not install the plugin in napari as software.*