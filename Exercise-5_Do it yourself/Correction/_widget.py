"""
This module is an example of a barebones QWidget plugin for napari

It implements the Widget specification.
see: https://napari.org/stable/plugins/guides.html?#widgets

Replace code below according to your needs.
"""
from typing import TYPE_CHECKING
from napari.types import ImageData, LabelsData
from magicgui import magic_factory
from qtpy.QtWidgets import QHBoxLayout, QPushButton, QWidget

from skimage.io import imread
from skimage.color import rgb2gray
from skimage.filters import threshold_otsu, threshold_li, threshold_yen
from collections import Counter

if TYPE_CHECKING:
    import napari


class ExampleQWidget(QWidget):
    # your QWidget.__init__ can optionally request the napari viewer instance
    # in one of two ways:
    # 1. use a parameter called `napari_viewer`, as done here
    # 2. use a type annotation of 'napari.viewer.Viewer' for any parameter
    def __init__(self, napari_viewer):
        super().__init__()
        self.viewer = napari_viewer

        btn = QPushButton("Click me!")
        btn.clicked.connect(self._on_click)

        self.setLayout(QHBoxLayout())
        self.layout().addWidget(btn)

    def _on_click(self):
        print("napari has", len(self.viewer.layers), "layers")


@magic_factory
def example_magic_widget(img_layer: "napari.layers.Image"):
    print(f"you have selected {img_layer}")
    
@magic_factory(call_button="Run", filter_selected={"choices": ['otsu', 'li','yen']})
def threshold_f(selected_image: ImageData,filter_selected='otsu') -> LabelsData:
    gray_ = rgb2gray(selected_image) # rgb image to gray image
    if filter_selected == 'otsu':
        ths = threshold_otsu(gray_) # determine threshold with otsu method
    elif filter_selected == 'li':
        ths = threshold_li(gray_) # determine threshold with li method
    elif filter_selected == 'yen':    
        ths = threshold_yen(gray_) # determine threshold with yen method
    mask = (ths > gray_) # apply the threshold to the image
    return mask

@magic_factory(result_widget=True)
def leaf_area(mask: "napari.layers.Labels"):
    current_mask = mask.data
    dico = dict(Counter(current_mask.flatten())) # Total number of black and white pixel
    labels_leaf_area = dico[True]
    print('Leaf Area:',labels_leaf_area) # Get total number of white pixel
    return labels_leaf_area

# Uses the `autogenerate: true` flag in the plugin manifest
# to indicate it should be wrapped as a magicgui to autogenerate
# a widget.
def example_function_widget(img_layer: "napari.layers.Image"):
    print(f"you have selected {img_layer}")
