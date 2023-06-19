# `REPO_ROOT/src/rain/cli` contains executable entry point scripts that are provided by this
# package. You need to install `rain` for these scripts to work.
# Compare this against `REPO_ROOT/scripts` which contains executable scripts needed to build this
# package.
import click
import random

from rain import load_mathematicians  # defined in rain/__init__.py


@click.command()
@click.option('--times', default=5, help='Makes it rain')
def make_it_rain(times):
    mathematicians = load_mathematicians()
    for _ in range(times):
        samples = random.sample(mathematicians, 10)
        print(', '.join(samples))
