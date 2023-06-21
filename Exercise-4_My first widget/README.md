# My first widget

## Script

The script is contained in the notebook `leaf_area.ipynb`.

## Add a widget

Here, we integrate a python script into widget. We are using three files to integrate the widget:

- `_widget.py` contains the widget codes

- `__init__.py` contains all the functions needed to initialise modules and control imports

- `napari.yaml` contains all the metadata and configuration information

## GUI for widget

There are many libraries designed to build a graphical user interface (GUI). For example, Tkinter or PyQt5. On napari, PyQt5 is highly recommended for building a GUI. This advice is generally aimed at advanced programmers. Building a GUI requires a lot of time and code. As a result, it is very difficult for novice programmers to design a code from scratch.

### Magicgui

The napari community has created a **magicgui** library to shorten the process of creating a GUI. **magicgui** is a general abstraction layer on GUI toolkit backends (like Qt), with an emphasis on mapping python types to widgets. This library is aimed at programming novices. It makes building widgets to represent function inputs easy. Below is an illustration of how to use magicgui:

```
from magicgui import magicgui
import datetime
import pathlib

@magicgui(
    call_button="Calculate",
    slider_float={"widget_type": "FloatSlider", 'max': 10},
    dropdown={"choices": ['first', 'second', 'third']},
)
def widget_demo(
    maybe: bool,
    some_int: int,
    spin_float=3.14159,
    slider_float=4.5,
    string="Text goes here",
    dropdown='first',
    date=datetime.datetime.now(),
    filename=pathlib.Path('/some/path.ext')
):
    ...

widget_demo.show()
```

![Alt text](7586a2670f0eb26111339c8f0fe6f8c4651ee9a9f444584181967deeb4301c80.png)