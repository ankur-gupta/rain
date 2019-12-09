#! /usr/bin/env python
from __future__ import absolute_import  # No implicit relative imports
import click
import random
from rain import load_mathematicians  # defined in rain/__init__.py


@click.command()
@click.option('--times', default=5,
              help='Makes it rain')
def make_it_rain(times):
    mathematicians = load_mathematicians()
    for _ in range(times):
        samples = random.sample(mathematicians, 10)
        print(', '.join(samples))


if __name__ == '__main__':
    make_it_rain()
