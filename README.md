# 🌧️ rain

![GitHub](https://img.shields.io/github/license/ankur-gupta/rain?link=https%3A%2F%2Fgithub.com%2Fankur-gupta%2Frain%2Fblob%2Fmain%2FLICENSE)
![build](https://img.shields.io/github/actions/workflow/status/ankur-gupta/rain/build.yml)
![Codecov](https://img.shields.io/codecov/c/github/ankur-gupta/rain)
![GitHub Repo stars](https://img.shields.io/github/stars/ankur-gupta/rain)
![GitHub forks](https://img.shields.io/github/forks/ankur-gupta/rain)

**A live example to illustrate python packaging, testing, building, & deploying**

`rain` is an online reference that can be explored by
humans. It provides a living, dynamic alternative to commonly available 
[static documentation](https://packaging.python.org/en/latest/tutorials/packaging-projects/). This repository covers 
the following topics.

* file and directory type modules
* selective imports from a directory-type module
* relative imports
* circular imports
* storing and distributing data files
* entry point CLI scripts
* setup logging inside a package 
* storing version information in one location
* specifying dependencies
* running and skipping tests
* obtaining coverage metrics & uploading them to codecov.io
* building and installing this package locally
* example CI/CD using GitHub Actions
* adding badges to your README
* deploying to PyPI (explained but not demo'd)

## Aims
`rain` is a _live and unencumbered reference_ that aims to _educate not execute_.

### Online reference
`rain` uses [hatch](https://hatch.pypa.io/latest/) to build package, run tests, update version, and more. 
If you want to create an empty scaffold for a new package you should use 
[`hatch new my-project`](https://hatch.pypa.io/latest/intro/). `rain` provides an online reference you can peruse to 
learn about the topics mentioned above.

### Learn by examples
You can find all the details in a written, textual documentation. But, if you don't want to read the documentation 
and instead want to see a _living_ example, try `rain`. 

### Less code to browse through
You can find examples in any of the famous packages such as `numpy` but you'll have to browse through a lot of 
complexity. `rain` provides a small code base that is only sufficient to explain python packaging.

### Learn one topic at a time 
Most of the topics above are explained in individual modules and files. For example, 
[`circular_imports` module](https://github.com/ankur-gupta/rain/tree/main/src/rain/circular_imports) only deals with 
circular imports without having to deal with other issues such as logging. 

### Tests and builds via GitHub Actions
CI/CD is often best explained via live, working examples instead of written textual documentation.

### Clone/fork and experiment
Clone or fork `rain` to quickly test out something without having to write a new package from scratch or messing your 
own important package. 
 
## Directory Structure
```
.
├── LICENSE
├── README.md
├── pyproject.toml
├── src
│ └── rain
│     ├── __init__.py
│     ├── circular_imports
│     │ ├── __init__.py
│     │ ├── array.py
│     │ └── grouped_array.py
│     ├── cli
│     │ ├── __init__.py
│     │ └── rain_maker.py
│     ├── directory_module_with_selective_imports
│     │ ├── __init__.py
│     │ ├── main.py
│     │ └── utils.py
│     ├── local_imports
│     │ ├── __init__.py
│     │ ├── main.py
│     │ └── variables.py
│     ├── logging_example
│     │ ├── __init__.py
│     │ └── main.py
│     ├── resources
│     │ └── mathematicians.txt
│     ├── this_directory_is_a_module
│     │ ├── __init__.py
│     │ └── this_file_is_a_submodule.py
│     ├── this_file_is_a_module.py
│     └── version.py
└── tests
    ├── __init__.py
    ├── not_a_test_file.py
    ├── test_a_function_in_a_module.py
    ├── test_a_function_in_a_submodule.py
    ├── test_circular_imports.py
    ├── test_demo_use_of_local_imports.py
    ├── test_errors.py
    ├── test_how_to_import_from_package.py
    ├── test_markers.py
    ├── test_naming_conventions.py
    ├── test_root.py
    ├── test_this_function_will_be_imported.py
    ├── test_using_a_class.py
    └── test_version.py
```

## License
[MIT](https://github.com/ankur-gupta/rain/blob/main/LICENSE)

## Contributing
Contributions are welcome. If you find errors or identify need for
improvement, please look into
[Issues](https://github.com/ankur-gupta/rain/issues) and open an issue.