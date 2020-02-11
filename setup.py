from setuptools import setup

PACKAGE_NAME = 'rain'

# Read-in the version
# See 3 in https://packaging.python.org/guides/single-sourcing-package-version/
version_file = './{}/version.py'.format(PACKAGE_NAME)
version = {}
try:
    # Python 2
    execfile(version_file, version)
except NameError:
    # Python 3
    exec(open(version_file).read(), version)

# Read-in the README.md
with open('README.md', 'r') as f:
    readme = f.readlines()
readme = ''.join(readme)

setup(name=PACKAGE_NAME,
      version=version['__version__'],
      url='https://github.com/ankur-gupta/rain',
      author='Ankur Gupta',
      author_email='ankur@perfectlyrandom.org',
      description='Template python package',
      long_description=readme,
      long_description_content_type="text/markdown",
      keywords='template, python, package',
      packages=[PACKAGE_NAME,
                '{}.scripts'.format(PACKAGE_NAME),
                '{}.module_three'.format(PACKAGE_NAME)],
      package_data={PACKAGE_NAME: ['resources/*.txt']},
      include_package_data=True,
      entry_points='''
        [console_scripts]
        rain_maker=rain.scripts.rain_maker:make_it_rain
      ''',
      classifiers=[
          "License :: OSI Approved :: MIT License",
      ],
      install_requires=['click', 'six', 'numpy', 'future'],
      setup_requires=['pytest-runner'],
      # pytest-cov needed for coverage only
      tests_require=['pytest', 'pytest-cov'],
      zip_safe=True)

# Notes:
# (1) Script installs in user-site as a newly made binary file which
#     points to the script actually in the package.
# (2) Run tests from the repo root:
#        cd $REPO_ROOT
#        python3 -m pytest rain/tests
# (3) Install using pip in user-site/bin:
#        cd $REPO_ROOT
#        pip3 install --user ./
# (4) Designed to work with both python2 and python3 but only tested
#     on python3.
# (5) Run `rain_maker` after install from anywhere (assuming user-site/bin
#     is in the PATH):
#      rain_maker --help
#      rain_maker --times 10
#      rain_maker
