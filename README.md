# 🌧️ Rain
![build](https://github.com/ankur-gupta/rain/workflows/build/badge.svg)
[![codecov](https://codecov.io/gh/ankur-gupta/rain/branch/master/graph/badge.svg)](https://codecov.io/gh/ankur-gupta/rain)

**A living template for python packaging, testing, building, & deploying**

This python package provides a template for other python packages. The aim
is to serve as a live, working template that can be explored visually by
humans to understand and perhaps copy/paste from. In other words,
`rain` serves as a living, dynamic alternative to static documentation.
This template covers these topics.

* correct way of importing within packages
* entry point scripts
* storing data files
* properly storing version information in one location
* specifying dependencies
* obtaining coverage metrics and uploading them to a website like codecov.io
* installing and uninstalling this package locally
* building this package locally
* example CI/CD using GitHub Actions
* deploying to PyPI
* adding badges to your README

## Folder Structure
```
.
├── .coveragerc
├── .gitignore
├── README.md
├── requirements.txt
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

### Why do we define dependencies in both `setup.py` and `requirements.txt`?
Both these files serve different objectives that are somewhat mutually
exclusive and therefore we often need both. This
[Stack Overflow post](https://stackoverflow.com/questions/43658870/requirements-txt-vs-setup-py)
describes this issue quite well. This post also describes how you can
only list the dependencies in `setup.py` and "link" them in `requirements.txt`.
Expanding upon this post:

#### `requirements.txt`
- helps you setup your environment in "one fell swoop"
- can be used by `pip` instead of using `python setup.py`
- makes setting up virtual environments easy
- lets you install dependencies of a package easily without having to install
the package (`rain`, in this case) itself. This is especially useful for
CI/CD pipelines (see [an example in `rain`](https://github.com/ankur-gupta/rain/blob/master/.github/workflows/build.yml#L22)).
- allows you to install packages that are not necessarily dependencies of
your package. For example, your package (eg: `rain`) may not depend on
`pandas` but `pandas` may be a commonly used package that is used alongside
`rain`. In such a case, it may not be appropriate to put `pandas` in
`setup.py`'s `install_requires`, `setup_requires`, `tests_require`, or
`extras_require`. One reason is that while _you_ may use `pandas` alongside
`rain` but not everyone else will.
 - is easier to edit than `setup.py` and allows comments

 #### `setup.py`
 - helps you install all dependencies when installing the package (depending
 upon options used with `python setup.py install`)
 - ensures that all specified dependencies of the package are installed
 before you install the intended package
 - specifies only those dependencies that are necessary for the
 packages

## Run Code
You don't need to install the package to use the code. You just need to
be in `$REPO_ROOT`. The following example (if it runs) verifies that a
complicated importing situation within a package correctly works.
```bash
# In $REPO_ROOT
python3 -c "from rain import banana; print(banana())"
# plantain
```

## Run Tests
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

### Run script to check your installation
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

## Build Package Locally
You can build a tarball and a wheel like so.
```bash
# Ensure that the package `wheel` installed.
cd $REPO_ROOT
python setup.py sdist bdist_wheel
# Check $REPO_ROOT/dist for both tarball and wheel files.
```
If you encounter an
[error](https://stackoverflow.com/questions/34819221/why-is-python-setup-py-saying-invalid-command-bdist-wheel-on-travis-ci)
like `error: invalid command 'bdist_wheel'`,  you may not have `wheel`
package installed. You can install `wheel` via `pip`:
```bash
pip install --user wheel
```

## Example CI/CD using GitHub Actions
Setting up CI/CD depends on the CI/CD platform you are using. As of writing
this README, there is no universal CI/CD. However, most modern CI/CD follow
the same overall process:

1. Define the CI/CD steps in some `.yml` file that is stored in the repository
as a git-tracked file. You can have multiple `.yml` files defining different
steps for different purposes. Here are some common steps. Not all workflows
may include all of these steps.
    - setup the test environment
    - pull your repository with the changes that need to be tested/deployed
    - run tests, possibly in various versions of python
    - get code coverage metrics
    - upload the coverage metrics to a website like codecov.io
    - build the package
    - upload the package as an artifact (eg: tarball or a wheel)
    - deploy the package to run in production
2. Define trigger(s) than runs the steps specified in the `.yml` file. Here are
some examples of triggers. Of course, you can define other triggers.
    - a push to `master`, as well as
    - a pull request to merge to `master`
    - _cutting_ a release (eg: by `git tag`ing a commit on `master`)
3. The steps defined in a `.yml` file are typically run in an ephemeral virtual
machine or a docker container that
[exists only for the purpose](https://www.youtube.com/watch?v=qUYvIAP3qQk)
of implementing CI/CD.

GitHub Actions is one CI/CD framework. You can see the corresponding
YAML files in
[`.github/workflows`](https://github.com/ankur-gupta/rain/tree/master/.github/workflows).

## Uploading coverage metrics to codecov.io
The
[`build.yml`](https://github.com/ankur-gupta/rain/blob/master/.github/workflows/build.yml)
workflow shows this example with comments. The process has two main parts:
- Generate coverage report (typically as an XML file) using `pytest` and
`pytest-cov` (via [`coverage.py`](https://coverage.readthedocs.io/en/coverage-5.0.3/#using-coverage-py)).
See [this section in `build.yml`](https://github.com/ankur-gupta/rain/blob/master/.github/workflows/build.yml#L30).
- Upload the coverage report to codecov.io.
See [this section in `build.yml`](https://github.com/ankur-gupta/rain/blob/master/.github/workflows/build.yml#L37).

## Releasing
Releasing your package essentially involves attaching a sensible version
(eg: using [Semantic Versioning](https://semver.org/)) to your code and
releasing the code as a distributeable (eg: a tarball or a wheel). There are
various automated ways to "cutting a release" which we don't cover here.
Instead, we note the individual steps involved.

### Version in `setup.py`
The version in `setup.py` is the canonical source of truth for the version.
This is the version used by `python setup.py sdist bdist_wheel`. The
resulting files (tarball, wheel) in `$REPO_ROOT/dist` folder are named
using the version specified in `setup.py` as the `version` argument to
`setuptools.setup()` function. These are some example filenames:
```bash
$ cd $REPO_ROOT
$ ls dist/
rain-0.0.1-py3-none-any.whl
rain-0.0.1.tar.gz
```
Typically, we want to make the package version available to the python
interpreter as well. However, we want to store the version exactly once
within the source code -- this way we only have to modify it at one place
when we release a new version. There are
[various ways](https://packaging.python.org/guides/single-sourcing-package-version/)
to do this and we follow one specific method in `rain`.

- We define the version as a `str`-valued variable called `__version__` in
[`version.py`](https://github.com/ankur-gupta/rain/blob/master/rain/version.py).
- We execute [`version.py`](https://github.com/ankur-gupta/rain/blob/master/rain/version.py)
inside `setup.py` file in a particular way, as shown
[here](https://github.com/ankur-gupta/rain/blob/master/setup.py#L5). This
is done for two reasons (a) compatibility between python 2 and python 3,
(b) avoiding referencing the variable `__version__` without defining it
(while it would be legal python syntax to execute `version.py` and
reference `__version__`, linters and IDEs flag that as an error)
- We import `__version__` in
[`__init__.py`](https://github.com/ankur-gupta/rain/blob/master/rain/__init__.py#L3).

### Version via `git tag`
We can `git tag` a commit (on an appropriate branch such as `master`
or `release`) with a version string. Note that even though we use `git tag`
to mark versions,
[git tags](https://git-scm.com/book/en/v2/Git-Basics-Tagging)
are not specific to versions (you can do `git tag rick-and-morty`; git won't
care). We can do this via command line or via
[GitHub Web UI](https://github.com/ankur-gupta/rain/releases/new)
(recommended).
An example of command line example is:
```bash
cd $REPO_ROOT
# Commit all changes and ensure you're on the correct branch
git tag x.y.z

# Push the tags upstream. Push only the tag you made. Note that
# `git push origin --tags` will push all the tags which can cause problems.
git push origin x.y.z
```
On GitHub, releases are available on the
[Releases page](https://github.com/ankur-gupta/rain/releases). This works
even for tags generated from command line (as shown above) but it's better
to [Draft a new release](https://github.com/ankur-gupta/rain/releases/new)
via GitHub webpage because it lets you easily write good release notes.

Note the version in `git tag` may not be the same as the version in `setup.py`.
Conflicts between the version in `git tag` and version in `setup.py` can cause
CI/CD errors.

### Steps to follow
The following steps when performed in order helps you avoid CI/CD errors.
1. Commit all code changes to `master` (typically via a pull request).
2. Pull all changes to `master` locally.
    ```bash
    git checkout master
    git pull
    ```
3. Create a new branch off of `master`. Let's call this new branch
`release-new-version`.
    ```bash
    git checkout master
    git checkout -b release-new-version
    ```
4. Bump up the version in
[`version.py`](https://github.com/ankur-gupta/rain/blob/master/rain/version.py).
Ensure that the new version string is something that has never been used before.
This is important or you may get errors when you deploy and you may have to
repeat all of the steps.
5. Push the new branch to GitHub
    ```bash
    git push --set-upstream origin release-new-version
    ```
6. Create a pull request from `release-new-version` to `master`. This can be
done via GitHub webpage. The benefit of bumping up the version via a PR
is that you can run your CI/CD workflow on the PR. Typically, this CI/CD
builds a python package (even if it doesn't deploy it) and can find errors
before you finally merge.
7. Once you've verified that everything looks good, merge the PR to `master`
(after getting approval of reviewers, if necessary). At this point, any build
off of `master` would have the latest version. If you have CI/CD pipeline that
runs on merge to master, let it run to confirm that everything looks good.
8. Now, when you're sure that everything is good, `git tag` the commit on
`master` either via command line or via GitHub releases (recommended), as
discussed in the subsection above.
9. At this point, if you have a CI/CD pipeline setup to deploy the package
(such as to an artifact repository or PyPI), it will run and deploy your
package.

## Deploying to PyPI
Since I don't own the name `rain` on PyPI (and, at this point, I don't want to
change the name of my package), I don't have a live example of deploying this
package on PyPI.

Please be careful before deploying a package to PyPI (or Test PyPI).
PyPI and Test PyPI are open to the public and once a package is uploaded, it
might not be possible to undo it. You don't want to accidentally upload any
proprietary or private company code/data to PyPI (or Test PyPI).

Note that you cannot overwrite an existing version of your package on PyPI
(or Test PyPI). For example, if you've already uploaded version 0.1.2 to
PyPI (or Test PyPI), you cannot modify the source and overwrite the same
version 0.1.2 on PyPI (or Test PyPI). You must bump the version up and then
deploy again. This is because someone else might've written code against
version 0.1.2 and we don't want to break their code.

### Deploying from local machine
We can also deploy by building the package locally and then using
`twine` to upload the builds to PyPI. Note that you will need an account on
PyPI and on Test PyPI (optional but recommended). While uploading the package
to PyPI (or Test PyPI), you will need to enter your account password.
This prevents any random person from uploading a new version of your package.
These are the typical instructions but they're not relevant to `rain`,
as mentioned above.
```bash
cd $REPO_ROOT

# Clean the git state. An unclean git state (even untracked files) can
# accidentally be included in your build if you're not careful.

# Build the package locally (requires `wheel` package to be installed).
# See $REPO_ROOT/dist for the tarball and the wheel
python setup.py sdist bdist_wheel

# Upload to PyPI (or Test PyPI)
# Requires `twine` package to be installed (`pip install --user twine`).
twine upload --verbose --repository testpypi dist/*
twine upload --verbose --repository pypi dist/*
```

Note that you may need to add the following lines to your `$HOME/.pypirc`:
```
[distutils]
index-servers =
  pypi
  testpypi

[pypi]
username=<your-pypi-username>

[testpypi]
username=<your-testpypi-username>
```

### Deploying via GitHub Actions
We can use GitHub Actions to define a workflow that publishes to
Test PyPI and production PyPI. `rain` doesn't contain such as example but
you can see an example in another python package called
[flicker](https://github.com/ankur-gupta/flicker/blob/master/.github/workflows/pypi.yml).
The official instructions provide some more
[detail](https://packaging.python.org/guides/publishing-package-distribution-releases-using-github-actions-ci-cd-workflows/).

### Note about using Markdown-formatted `long_description`
Many repositories use Markdown-formatted `README.md` as the value to the
`long_description` argument in `setuptools.setup()` in `setup.py`. This
is especially true for GitHub repositories and `rain` itself does
[this](https://github.com/ankur-gupta/rain/blob/master/setup.py#L16).

PyPI, by default, expects `long_description` in reStructuredText. If a
Markdown-formatted `long_description` is provided when PyPI is expecting
reStructuredText,  publishing to PyPI fails with an error message like this:
```text
HTTPError: 400 Client Error: The description failed to render in the default
format of reStructuredText. See https://test.pypi.org/help/#description-content-type
for more information.
```
Luckily, this can be easily fixed by simply
[providing the markup format](https://packaging.python.org/tutorials/packaging-projects/#creating-setup-py)
in `setup.py`:
```python
setup(
    ...,
    long_description=readme,
    long_description_content_type="text/markdown",
    ...)
```
See the example in this repository
[here](https://github.com/ankur-gupta/rain/blob/master/setup.py#L28).
Also, see the FAQs on
[Test PyPI](https://test.pypi.org/help/#description-content-type)
or [PyPI](https://pypi.org/help/#description-content-type).

## Adding badges to your README
Adding badges is a great way of letting people know about key information.
See the top of this
[README file in raw format](https://raw.githubusercontent.com/ankur-gupta/rain/master/README.md)
to see the Markdown that include badges.

### GitHub Actions badge
After you've defined a Github Action (aka workflow), you can get the Markdown
for the badge from the
[GitHub Actions webpage](https://github.com/ankur-gupta/rain/actions).
Click on an event (eg: `build` for `rain`) and click on `Create Status badge`.
Here is an example:
```markdown
![build](https://github.com/ankur-gupta/rain/workflows/build/badge.svg)
```

### codecov.io coverage badge
Once you've added a GitHub repository to your codecove.io account, you can
obtain the badge Markdown from the "Badge" tab in the "Settings" page.
Here is an example:
```markdown
[![codecov](https://codecov.io/gh/ankur-gupta/rain/branch/master/graph/badge.svg)](https://codecov.io/gh/ankur-gupta/rain)
```

### PyPI version badge
If you package is on PyPI, you can generate a badge Markdown from a third-party
website such as [shields.io](https://shields.io/) or
[badge.fury.io](https://badge.fury.io/). This is an example Markdown for
another package (because this package is not the `rain` package on PyPI).
```markdown
[![PyPI Latest Release](https://img.shields.io/pypi/v/flicker.svg)](https://pypi.org/project/flicker/)
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
