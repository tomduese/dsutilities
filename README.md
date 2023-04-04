# ds-utilities
This repository contains a bunch of functions for recently used functions in data science. The idea is to use it as a git submodule in any given repository you are working on. To add a submodule to a repository you can find information here. https://git-scm.com/book/en/v2/Git-Tools-Submodules

### Environment

This repo contains a requirements.txt file with a list of all the packages and dependencies you will need. Before you install the virtual environment, make sure to install postgresql if you haven't done it before.

```bash
brew update
brew install postgresql
```

In order to install the environment you can use the following commands:

```
pyenv local 3.9.8
python -m venv .venv
source .venv/bin/activate
pip install --upgrade pip
pip install -r requirements.txt
```

