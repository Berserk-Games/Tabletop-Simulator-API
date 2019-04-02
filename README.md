# Tabletop Simulator API

This is the source of the api documentation in Tabletop Simulator. It uses a modified version of [Material-Design](https://github.com/squidfunk/mkdocs-material) for MkDocs.

## How it Works

The `.md` files in the `/docs` folder are written in Markdown, which is an easy-to-use markup language to add formatting to text. Additionally, some custom CSS is used, as well as a handful of custom images. When making changes, it is possible to live-preview them as you go if you have set up the local files for mkdocs + material design.

Alternatively, you can make modifications to individual pages then submit them for review. The developers will always be the ones to build and publish the site anyway, all you will do is modify the contents of this Git.

## Contributing

The API website is built using [MkDocs](https://www.mkdocs.org/) and several related extensions.

Pull requests are welcome, however in order to preview your changes, you must follow the instructions below:

### Prerequisites

You will need to ensure Python `3.6` is installed on your system.

If your system doesn't have it installed, you can either [download directly](https://www.python.org/downloads/release/python-366/) or install from a Python version manager such as [pyenv](https://github.com/pyenv/pyenv).

We utilise Pipenv and a `Pipfile` to ensure builds are consistent. If you don't already have Pipenv installed, please follow the official [pipenv install instructions](https://pipenv.readthedocs.io/en/latest/install/#installing-pipenv) for you platform.

### Installing Dependencies

Once've you installed the prerequisites, you must initialize your environment. From command line, this is done with:

```
pipenv install
```

You can then "activate" this environment with:

```
pipenv shell
```

### Previewing

Once your Pipenv environment is activated, you can simply execute:

```
mkdocs serve
```

Then open your browser and navigate to `http://localhost:8000` in order to view your changes.
