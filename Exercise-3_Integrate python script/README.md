# Integrating a python script into the plugin

## Python script

The script is contained in the `seuillage.py`

## Integration

I- Integrate the script into `_widget.py`

1- We're going to create a function to contain the script

```
def threshold_f(current_image):
    ###
    SCRIPT
    ###
    return mask
```

*See correction:*

2- Putting a decorator above the function

We're going to create a user interface to handle the script input

```
@magicgui(call)
def threshold_f(current_image):
    ###
    SCRIPT
    ###
    return mask
```

*See correction:*

II- Intégrer la fonction dans le manifest `napari.yaml`

```
command
```

*See correction:*

III- Integrate the function in the file `__init__.py`

```
from sd
```

*See correction:*

IV- Integrate relevant packages into `setup.cfg`

```
skimage
```

*See correction:*

V- Integrate test function in the file `test_widget.py`

*See correction:*

VI- Include some information about your plugin into `README.md`

*See correction:*

VII- When it's over, install plugin **in your computer** with in `napari-thresholds` directory where `pyproject.toml` is located

```
pip install -e .
```

*Note: You install plugin in napari as python package. This command will not install the plugin in napari as software.*

Appendice:

VIII- How to make the plugin visible in the built-in napari

Be at `napari-thresholds` directory where `pyproject.toml` is located

Prerequisite: 
- Account Pypi
- Account Github

Protocol to deploy your plugin:
- API token

    1. Generate an API token at PyPi
    2. Create a new encrypted secret in napari-threshoolds github repository with the name "TWINE_API_KEY"

- Create a build

Make sure your build tool is up to data

```
python -m pip install --upgrade build
```

Create a build in napari-gtlearning folder

```
python -m build
```

- Upload package to the PyPI

Install Twine

```
python-m pip install --upgrade twine
```

Upload all of the archives under dist

```
twine upload --repository-url https://upload.pypi.org/legacy/ dist/*
```