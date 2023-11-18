# File Organization and PDF Merging Script | Enneas

[![License](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![Python Version](https://img.shields.io/badge/Python-3.6%2B-blue.svg)](https://www.python.org/downloads/)

A Python script for organizing images into subfolders and creating pdf out of them.
## Table of Contents

- [Installation](#installation)
- [Code Structure](#usage)
- [Contributing](#contributing)
- [License](#license)

## Installation

It is recommended to use pyenv, a CLI tool that allows multiple versions of Python to be installed separately. Follow the installation instructions for your platform and run:
```bash
pyenv install
```

This will download and install Python 3.10.11 which is specified in the .project-version file which in turn is created by the command pyenv local 3.10.11. This use of pyenv ensures the pinning and usage of the specified Python version.

>Note: pyenv downloads and compiles the version of Python you install, which means you may need to also install some libraries if not present in your system, please follow the common build problems wiki for your platform.

>If you already have Python 3.10.11 installed you do not need to reinstall it and pyenv should automatically use the correct version due to the pinning file .project-version


Create a virtualenv:


```bash
  python -m venv .venv
  source .venv/bin/activate
```

This virtualenv now has the version of Python which was set by pyenv and the .project-version file.

>Note: the rest of these instructions assume you've activated the virtualenv as does the Makefile. You may want to use a virtualenv tool like virtualenvwrapper or pyenv-virtualenv.

Install dependencies via the requirements.txt file located in this project:

```bash
  pip install -r requirements.txt
```

Run file. 
On terminal press:
```bash
  python main.py
```

## Code Structure
```
.
├── pictures                    # Directory where assignments' images exit
│   └──  pdf                    # Empty Directory for pdfs to be created
├── .gitignore                  # File for ignoring files in git
├── enneas.assign.py            # File calling the functions that contains the business logic of the python project 
├── main.py                     # File for running the python project
├── requirements.txt            # File for any Python packages to be installed
├── utils.py                    # File that contains the 3 Functions of the business logic: 1.create_requested_subfolders def for created the subfolders 00,01,02,  2.move_files def for moving images to the correct folder based on their prefix, 3.pdf_creator def for creating the required pdf with the sorted images
├── variable.py                 # File that contains the 2 Variables that are used in every function. 1.picture_path the path in which anyone can find the images of the project and 2. a List that contains the requested subfolders names.
```

## Installation

How can you contribute
1. Fork the repository
2. Create a new branch:
```bash
  git checkout -b feature-name
```
3. Make your changes and commit:
```bash
  git commit -m 'Add new feature'
```
4. Push to the branch:
```bash
  git push origin feature-name
```
5. Submit a pull request

## License
This project is licensed under the MIT License.
