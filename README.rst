=============================
Helpers for Using R in Python
=============================

R users are spoiled by a lack of fuss because it's a cushy,
purpose-built environment.  You plot things with "plot", you scale
things with "scale", and you get the norm with "norm".  You don't
write a lot of extra stuff, like "import", unless you want great
looking plots, in which case you use ``library(lattice)``.

When I'm using Python, I miss lattice.  I can use it via rpy2, but
doing that requires a lot of boilerplate code.  I'm trying to put that
noise in here.  An example usage is in the ``main`` function of the
``rpy2_helpers.py`` file.

Example usage in iPython
------------------------

This example shows how to do a simple scatterplot.

::

    import numpy as np
    from rpy2_helpers import xyplot
    
    x = np.random.random_integers(1, 100, 100)
    y = np.log(x)
    
    xyplot('y ~ x', {'x': x, 'y': y})

Here's a simple box and whisker plot.

::

    import numpy as np
    from rpy2_helpers import bwplot

    x = np.random.normal(size=100)
    # make it positive-heavy
    x = np.concatenate((x, 3 * (x + x.max())))
    big = x > 0
    bwplot('~ x | big', {'x': x, 'big': big})