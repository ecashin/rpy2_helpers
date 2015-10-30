"""rpy2_helpers - Avoid some boilerplate rpy2 usage code

Mostly I wrote this so that I can use xyplot without having
to remember a lot of details.

"""

import rpy2.robjects
from rpy2.robjects import DataFrame, Formula, globalenv, numpy2ri
from rpy2.robjects.packages import importr


# Automatically convert numpy arrays to R vectors.
numpy2ri.activate()


grdevices = importr('grDevices')
lattice = importr('lattice')
robjects = rpy2.robjects
rprint = globalenv.get("print")


DOC_TPT = """Call `{}` with the given `formula` and `data`.

You can supply `formula` as a string or rpy2 `Formula`.

You can supply `data` as a dict or rpy2 `DataFrame`.

"""


def do_plot(plot_fn, formula, data, **kwargs):
    if not isinstance(data, DataFrame):
        data = DataFrame(data)
    if not isinstance(formula, Formula):
        formula = Formula(formula)
    plot = plot_fn(
        formula, data, **kwargs)
    rprint(plot)


def bwplot(formula, data, **kwargs):
    do_plot(lattice.bwplot, formula, data, **kwargs)


bwplot.__doc__ = DOC_TPT.format('bwplot')


def xyplot(formula, data, **kwargs):
    do_plot(lattice.xyplot, formula, data, **kwargs)


xyplot.__doc__ = DOC_TPT.format('xyplot')
