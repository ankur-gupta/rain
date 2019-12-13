# Rain

## A template for python packaging
This python package provides a template for other python packages.
This template contains:

* correct way of importing within packages
* entry point scripts
* data files
* version information
* coverage

This is the folder structure:
```
.
├── .coveragerc
├── .gitignore
├── README.md
├── rain
│   ├── __init__.py
│   ├── compat.py
│   ├── module_fruits.py
│   ├── module_one.py
│   ├── module_plantain.py
│   ├── module_three
│   │   ├── __init__.py
│   │   ├── submodule_one.py
│   │   └── submodule_two.py
│   ├── module_two.py
│   ├── resources
│   │   └── mathematicians.txt
│   ├── scripts
│   │   ├── __init__.py
│   │   └── rain_maker.py
│   ├── tests
│   │   ├── __init__.py
│   │   ├── test_module_fruits.py
│   │   └── test_module_one.py
│   └── version.py
└── setup.py
```

The template is designed to work with both python2 and python3 but is only
tested on python3, as of now. Throughout this documentation, `python3`
typically refers to the user-site python installations that are outside
the virtual environments. Within a virtual environment, replace `python3` with
`python`. Same goes for `pip3` to `pip`.

## Run code
You don't need to install the package to use the code. You just need to
be in `$REPO_ROOT`. The following example (if it runs) verifies that a
complicated importing situation within a package correctly works.
```bash
# In $REPO_ROOT
python3 -c "from rain import banana; print(banana())"
# plantain
```

## Run tests
### Run selected tests
Run tests from `$REPO_ROOT`; you will get an error otherwise. You don't need
to install the package to run tests. See
[pytest documentation](http://doc.pytest.org/en/latest/example/markers.html)
for more examples.
```bash
# In $REPO_ROOT
# Run all tests without coverage
python3 -m pytest rain/tests

# Run only the "sleepy" tests
python3 -m pytest -m sleepy rain/tests

# Run the non-sleepy tests
python3 -m pytest -m "not sleepy" rain/tests

# Run tests that are sleepy but not random
# You can use any valid python syntax within quotes ""
python3 -m pytest -m "sleepy and (not random)" rain/tests"
```
Make sure that the markers are defined in `$REPO_ROOT/pytest.ini` to avoid
a warning.

### Run tests with coverage
You need to install `pytest-cov` for this to work. See
[pytest-cov documentation](https://pytest-cov.readthedocs.io/en/latest/readme.html#usage)
for more details.

#### Without a `.coveragerc` file
By default, you can get coverage for everything including
the tests. The tests typically have 100% coverage (unless you don't run
specific tests) which inflates the coverage metrics.
```bash
# In $REPO_ROOT with .coveragerc file deleted

# Get coverage for all tests
python3 -m pytest --cov=rain rain/tests

# Get coverage for only the "sleepy" tests. This will make the coverage
# for some test files be less than 100%.
python3 -m pytest -m sleepy --cov=rain rain/tests

# Get coverage for only the non-"sleepy" tests. This will make the coverage
# for some test files be less than 100%.
python3 -m pytest -m "not sleepy" --cov=rain rain/tests
```
Typical example:
```bash
# In $REPO_ROOT with .coveragerc file deleted
$ python3 -m pytest --cov=rain rain/tests
...
---------- coverage: platform darwin, python 3.7.3-final-0 -----------
Name                                 Stmts   Miss  Cover
--------------------------------------------------------
rain/__init__.py                        17      6    65%
rain/compat.py                           5      2    60%
rain/module_fruits.py                    9      1    89%
rain/module_one.py                       9      0   100%
rain/module_plantain.py                  6      0   100%
rain/module_three/__init__.py            2      0   100%
rain/module_three/submodule_one.py       8      1    88%
rain/module_three/submodule_two.py       7      1    86%
rain/module_two.py                       9      0   100%
rain/scripts/__init__.py                 0      0   100%
rain/scripts/rain_maker.py              12     12     0%
rain/tests/__init__.py                   0      0   100%
rain/tests/test_module_fruits.py        10      0   100%
rain/tests/test_module_one.py           17      0   100%
rain/version.py                          1      0   100%
--------------------------------------------------------
TOTAL                                  112     23    79%
```

#### With a `.coveragerc` file
To exclude the tests from coverage calculation, put a `.coveragerc` file
in `$REPO_ROOT`. See more details at
[Coverage.py documentation](https://coverage.readthedocs.io/en/latest/source.html).
See [`$REPO_ROOT/rain/.coveragerc`](https://github.com/ankur-gupta/rain/blob/master/.coveragerc)
as an example. You can run the same commands as above.

The following is a typical output in which we run all the tests but don't
count `$REPO_ROOT/rain/tests` and `$REPO_ROOT/rain/scripts` in the total
coverage percentage.
```bash
# In $REPO_ROOT with .coveragerc file present
$ python3 -m pytest --cov=rain rain/tests
...
---------- coverage: platform darwin, python 3.7.3-final-0 -----------
Name                                 Stmts   Miss  Cover
--------------------------------------------------------
rain/__init__.py                        17      6    65%
rain/compat.py                           5      2    60%
rain/module_fruits.py                    9      1    89%
rain/module_one.py                       9      0   100%
rain/module_plantain.py                  6      0   100%
rain/module_three/__init__.py            2      0   100%
rain/module_three/submodule_one.py       8      1    88%
rain/module_three/submodule_two.py       7      1    86%
rain/module_two.py                       9      0   100%
rain/version.py                          1      0   100%
--------------------------------------------------------
TOTAL                                   73     11    85%
```

## Installation & Uninstallation
### Install outside a virtual environment
Install using `pip` at user-site instead of `python setup.py`. This makes it
easier to uninstall. The script `rain_maker` is installed in user-site/bin.
```bash
# Installation
# In $REPO_ROOT
pip3 install --user ./

# Uninstallation
# From any location. This will uninstall the script `rain_maker` as well.
pip3 uninstall rain
```

### Install within a virtual environment
```bash
# For fish shell that has virtualfish installed
vf new rain  # Uses Python 3 by default
vf activate rain
which pip  # Check that this is the pip in the `rain` virtualenv
pip install ./
pip uninstall rain  # Try repeatedly until `pip show rain` is clean
pip show rain
vf deactivate
```

## Run script to check your installation
```bash
# From anywhere when installed outside the virtual environment
# and assuming user-site/bin is is your PATH.
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

## Correct way to do intra-package imports
Python importing is complicated. These links provide good information:
* [Comprehensive guide](https://chrisyeh96.github.io/2017/08/08/definitive-guide-python-imports.html)
* [PEP420](https://www.python.org/dev/peps/pep-0420/) talks about about namespace
packages
* [PEP328](https://www.python.org/dev/peps/pep-0328/) talks about relative and
absolute imports

But, here I provide a quick guide. There are four types of imports:
- Absolute import
    - Absolute "full-path" import
    - Absolute "non-full-path" import
- Relative import
    - Explicit relative import
    - Implicit relative import

```python
# Absolute "non-full-path" import
# Standard way for client code to use a package. Package typically is
# installed but need not be installed if running the following line is run
# in $REPO_ROOT. This is also used in test files; see
# $REPO_ROOT/rain/tests/test_*.py for more details.
from rain import function_one

# Absolute "full-path" import
# Recommended way to perform intra-package imports. See example in
# $REPO_ROOT/rain/module_fruits.py and $REPO_ROOT/rain/__init__.py.
# This is typically not used for tests but can be used; see
# $REPO_ROOT/rain/tests/test_*.py for more details.
from rain.module_plantain import plantain

# Explicit relative import
# This is second-best for intra-package imports after the Absolute "full-path"
# import. Must start with `from`. The only way to perform relative imports
# in Python 3 or in Python 2 (with `absolute_import` imported). The following
# line should exist in a sibling file/module of
# $REPO_ROOT/rain/module_plantain.py.
from .module_plantain import plantain

# Implicit relative import
# Never use this. This is illegal in Python 3. In Python 2, this becomes
# illegal if we import `absolute_import` from `__future__`. The following line
# would exist in a sibling file/module of $REPO_ROOT/rain/module_plantain.py.
from module_plantain import plantain
```
See
[`$REPO_ROOT/rain/module_fruits.py`](https://github.com/ankur-gupta/rain/blob/master/rain/module_fruits.py) and
[`$REPO_ROOT/rain/__init__.py`](https://github.com/ankur-gupta/rain/blob/master/rain/__init__.py)
as examples.

See the [Stack Overflow post](https://stackoverflow.com/questions/5811463/when-to-use-absolute-imports)
that recommends using absolute full-path imports within a package, whenever
possible. But, explicit relative imports are okay.

### Check that everything imports correctly
You can run the following commands in one of two ways:
 - Run from `$REPO_ROOT` without installing the package. Event if you install
 the local one, _i.e._ `$REPO_ROOT` takes precedence over the installed code
 that is typically in user-site/bin.
- Run from outside `$REPO_ROOT` after installing the package.

The `banana()` function is the one with complicated import order issue but
should import correctly.
```python
from rain import (function_one, function_two, function_three, function_four,
                  apple, banana, plantain)
print(function_one())
print(function_two(1))
print(function_three())
print(function_four())
print(apple())
print(banana())
print(plantain())
# one
# one
# one
# four
# apple
# plantain
# plantain
```

## Troubleshooting
This section lists some common errors.

### Cannot import the package
##### Not listing the package(s) in `setup.py` file
This typically happens when you're sure that you've installed your package and
you're using the matching/corresponding version of python executable that
can find the package in the `site-packages` where the package was installed.
This might be because you forgot to provide the list of package(s) to
`setup()` in `setup.py` file. This is an example of what you should add:
```python
# In setup.py file
setup(...,
...,
packages=[PACKAGE_NAME,
          '{}.scripts'.format(PACKAGE_NAME),
          '{}.module_three'.format(PACKAGE_NAME)],
...)
```
If you don't list the package(s), then you might find that your package
installs but is actually empty in `site-packages` location.
