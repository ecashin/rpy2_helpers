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

You can provide the keywords that xyplot handles.

::

    import numpy as np
    from rpy2_helpers import xyplot
    
    x = np.arange(-4, 4, 0.1)
    y = np.tanh(x)
    
    xyplot('y ~ x', {'x': x, 'y': y}, main='tanh(x)')


Here's a simple box and whisker plot with two groups.

::

    import numpy as np
    from rpy2_helpers import bwplot

    x = np.random.normal(size=100)
    # make it positive-heavy
    x = np.concatenate((x, 3 * (x + x.max())))
    big = np.chararray(shape=x.shape, itemsize=5)
    big[x>0] = 'big'
    big[x<=0] = 'small'
    bwplot('~ x | big', {'x': x, 'big': big})


Fancy Example
-------------

If you want more fanciness, it's either dive into rpy2's details or go
to an R prompt.  The example below uses a custom panel function
(defined inside the R environment as function ``my.panel.fn``) to plot
a line along with the sigmoid function.

You can programmatically cause the display to go away with ``dev_off``.

::

    from time import sleep
    import numpy as np
    from rpy2_helpers import grdevices, robjects, xyplot
    
    x = np.arange(-4, 4, 0.1)
    y = 1/(1 + np.exp(-x))
    
    robjects.r('''
        my.panel.fn <- function(x, y, subscripts) {
    	    panel.xyplot(x, y)
    	    panel.lmline(x, y)
    	}
    ''')
    xyplot(
        'y ~ x',
    	{'x': x, 'y': y},
    	main='linear approximation to sigmoid',
    	panel=robjects.globalenv['my.panel.fn'])
    
    sleep(3)
    grdevices.dev_off()
