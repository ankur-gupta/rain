# Rain

## A template for python packaging
This python package provides a template for other python packages. This template contains:

* entry point scripts
* data files
* version information

This is the folder structure:

```
.
├── README.md
├── setup.py
├── rain
│   ├── __init__.py
│   ├── compat.py
│   ├── module_one.py
│   ├── module_two.py
│   ├── module_three
│   │   ├── __init__.py
│   │   ├── submodule_one.py
│   │   └── submodule_two.py
│   ├── scripts
│   │   ├── __init__.py
│   │   └── rain_maker.py
│   ├── tests
│   │   └── test_module_one.py
│   ├── resources
│   │   └── mathematicians.txt
│   └── version.py
└── .gitignore
```

The template is designed to work with both python2 and python3 but is only tested on python3,
as of now.

## Run tests
Run tests from $REPO_ROOT. You will get an error otherwise.
```bash
cd $REPO_ROOT
python3 -m pytest rain/tests
```

## Installation & Uninstallation
Install using `pip` at user-site instead of `python setup.py`. This makes it easier to uninstall.
The script `rain_maker` is installed in user-site/bin.

```bash
# Installation
cd $REPO_ROOT
pip3 install --user ./

# Uninstallation
# From any location. This will uninstall the script `rain_maker` as well.
pip3 uninstall rain

```

## Run script to check your installation
```bash
# From anywhere (assuming user-site/bin is is your PATH)
$ rain_maker --help
$ rain_maker --times 10
$ rain_maker
```

Sample output of `rain_maker` looks like:
```bash
$ rain_maker
Galois, Weirstrauss, Descartes, Euler, Cauchy, VonNeumann, Russell, Chebyshev, Newton, Leibniz
Russell, DeMoivre, Cauchy, Erdos, Bayes, Newton, Leibniz, Peano, Weirstrauss, Nash
Taylor, Galois, Godel, Riemann, Weirstrauss, Pythagoras, Leibniz, Chebyshev, Russell, Maxwell
Turing, Frege, Cantor, Bernoulli, Weirstrauss, Einstein, Boole, Kolmogorov, Gauss, Bayes
Godel, Poincare, Banach, Bernoulli, Newton, Maxwell, Lagrange, Huygens, Riemann, Chebyshev
```
