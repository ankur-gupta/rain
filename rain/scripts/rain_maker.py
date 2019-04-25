#! /usr/bin/env python
import click

import random
from rain import load_mathematicians


@click.command()
@click.option('--times', default=5,
              help='Makes it rain')
def make_it_rain(times):
    mathematicians = load_mathematicians()
    for _ in range(5):
        print(random.sample(mathematicians, 10))


if __name__ == '__main__':
    make_it_rain()
