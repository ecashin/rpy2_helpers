#! /usr/bin/env python2.7
"""Avoid some boilerplate rpy2 usage code with helpers.

Mostly I wrote this so that I can use xyplot without having
to remember a lot of details.

"""

import click
from rpy2.robjects import DataFrame, Formula, globalenv
from rpy2.robjects.packages import importr


grdevices = importr('grDevices')
lattice = importr('lattice')
rprint = globalenv.get("print")


def xyplot(formula, data, **kwargs):
    if not isinstance(formula, Formula):
        formula = Formula(formula)
    plot = lattice.xyplot(
        formula, data, **kwargs)
    rprint(plot)


@click.command()
def main():
    import numpy as np
    from rpy2.robjects import numpy2ri
    numpy2ri.activate()

    x = np.random.random_integers(0, 100, 100)
    x.sort()
    y = np.square(x)
    xyplot('y ~ x', DataFrame({'x': x, 'y': y}))
    raw_input('Hit enter to exit.')
    grdevices.dev_off()


if __name__ == '__main__':
    main()
