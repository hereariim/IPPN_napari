# How to make the plugin visible in the built-in napari

Be at `napari-thresholds` directory where `pyproject.toml` is located

Prerequisite: 
- **Account Pypi**
- **Account Github**

Protocol to deploy your plugin:

## API token

    1. Generate an API token at PyPi
    2. Create a new encrypted secret in napari-threshoolds github repository with the name "TWINE_API_KEY"

## Create a build

Make sure your build tool is up to date

```
python -m pip install --upgrade build
```

Create a build in napari-gtlearning folder

```
python -m build
```

## Upload package to the PyPI

Install Twine

```
python-m pip install --upgrade twine
```

Upload all of the archives under dist

```
twine upload --repository-url https://upload.pypi.org/legacy/ dist/*
```

## Napari-hub

Once deployed, the plugin is visible in the napari plugin library. Access to the plugin and its code is free.

![Capture d’écran 2023-06-24 001221](https://github.com/hereariim/IPPN_napari/assets/93375163/bf828a1a-6552-4751-85e2-e2dbc9ade73c)
