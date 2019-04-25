from setuptools import setup

PACKAGE_NAME = 'rain'

# Read-in the version
execfile('./{}/version.py'.format(PACKAGE_NAME))

# Read-in the README.md
with open('README.md', 'r') as f:
    readme = f.readlines()

setup(name=PACKAGE_NAME,
      version=__version__,
      url='https://github.com/ankur-gupta/rain',
      author='Ankur Gupta',
      author_email='ankur@perfectlyrandom.org',
      description='Template python package',
      long_description=readme,
      keywords='template, python, package',
      packages=[PACKAGE_NAME, '{}.scripts'.format(PACKAGE_NAME)],
      package_data={PACKAGE_NAME: ['resources/*.txt']},
      include_package_data=True,
      entry_points='''
        [console_scripts]
        rain_maker:rain.scripts.rain_maker:make_it_rain
      ''',
      install_requires=[],
      setup_requires=['pytest-runner'],
      tests_require=['pytest'],
      zip_safe=True)

# Notes:
# Script installs in user-site as a newly made binary file which
# points to the script actually in the package.
