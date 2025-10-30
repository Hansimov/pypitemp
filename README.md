# pypitemp
A template of pypi library

![](https://img.shields.io/pypi/v/pypitemp?label=pypitemp&color=blue&cacheSeconds=60)

## Create new project

Create new Github Repo.

Add GitHub Action Repository Secrets (Settings > Secrets and variables > Actions) with name `PYPI_TOKEN` for PyPI deployment.

Copy init file structure:

```sh
# ~/repos/pypitemp
python template.py -s "." -t "~/repos/tfmx" -n "tfmx" -d "Serve Transformers in one line" -v "0.0.1"
```

Init and point to remote github repo:

```sh
git init
git add .
git branch -M main
git commit -m ":gem: [Feature] init project"
git remote add origin https://github.com/Hansimov/tfmx.git
git push -u origin main
```

## Install package

```sh
pip install pypitemp --upgrade
```

## Usage

Run example:

```sh
python example.py
```

See: [example.py](https://github.com/Hansimov/pypitemp/blob/main/example.py)

```python
```
