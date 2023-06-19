# Create your plugin

First of all, we're going to create a directory that will contain the plugin structure. 

*Tips: You don't need a great deal of know-how to create the structure of a plugin. The cookiecutter function creates the structure directory for you*

In terminal, install cookiecutter with the following command

```bash
pip install cookiecutter
```

In terminal, create your directory with the following command

```bash
cookiecutter https://github.com/napari/cookiecutter-napari-plugin
```

Cookiecutter prompts you for information about your plugin and a new directory will be created in your current working directory

```bash
full_name [Napari Developer]: guest-0000
email [yourname@example.com]: guest-0000@gmail.com
github_username_or_organization [githubuser]: guest-0000_pizalliolo
# NOTE: for packages whose primary purpose is to be a napari plugin, we
# recommend using the 'napari-' prefix in the package name.
# If your package provides functionality outside of napari, you may
# choose to leave napari out of the name.
plugin_name [napari-foobar]: napari-thresholds
Select github_repository_url:
1 - https://github.com/guest-0000_pizalliolo/napari-thresholds
2 - provide later
Choose from 1, 2 [1]:
module_name [growth_cone_finder]: napari_thresholds
display_name [napari FooBar]: Thresholds
short_description [A simple plugin to use with napari]: Several thresholds available
include_reader_plugin [y]: n
include_writer_plugin [y]: n
include_sample_data_plugin [y]: n
include_dock_widget_plugin [y]: y
use_git_tags_for_versioning [n]: n
Select license:
1 - BSD-3
2 - MIT
3 - Mozilla Public License 2.0
4 - Apache Software License 2.0
5 - GNU LGPL v3.0
6 - GNU GPL v3.0
Choose from 1, 2, 3, 4, 5, 6 (1, 2, 3, 4, 5, 6) [1]: 1
```

You created a **minimal** napari plugin

```bash
napari-thresholds/
│
├── .github
│   └── workflows
│      └── test_and_deploy.yml
├── LICENSE
├── MANIFEST.in
├── napari_thresholds
│   ├── __init__.py
│   ├── _widget.py
│   ├── napari.yaml
│   └── _tests
│       ├── __init__.py
│       └── test_widget.py
├── pyproject.toml
├── README.md
├── setup.cfg
└── tox.ini
```