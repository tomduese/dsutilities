# dsutilities
This repository contains a bunch of functions for recently used functions in data science. The idea is to use it as a git submodule in any given repository you are working on. 

### Set up in parent repository
To add a submodule to a repository you can find information here https://git-scm.com/book/en/v2/Git-Tools-Submodules and you can run the following commands in the parent repository:

```bash
git submodule add git@github.com:tomduese/dsutilities.git
git commit -am "add dsutilities"
git push origin master
```
### Environment

This repo contains a requirements.txt file with a list of all the packages and dependencies you will need. Before you install the virtual environment. In order to install the environment you can use the following commands:


```bash
pyenv local 3.9.8
python -m venv .venv
source .venv/bin/activate
pip install --upgrade pip
pip install -r requirements.txt
```
Be aware in case you want to use the submodule to install the environment in the parent repository and change the the last line accordingly to `pip install -r dsutilities/requirements.txt`

