colwiseproportion
-----------------

Workbench module that converts numeric columns into proportions of their totals

Features
--------

* Lets the user choose columns.
* Throws an error on non-numeric columns.
* Writes new columns with 'percent' appended.

Developing
----------

First, get up and running:

#. ``python3 ./setup.py test`` # to test

To add a feature:

#. Write a test in ``test_colwiseproportion.py``
#. Run ``python3 ./setup.py test`` to prove it breaks
#. Edit ``colwiseproportion.py`` to make the test pass
#. Run ``python3 ./setup.py test`` to prove it works
#. Commit and submit a pull request

To develop continuously on Workbench:

#. Check this code out in a sibling directory to your checked-out Workbench code
#. Start Workbench with ``CACHE_MODULES=false bin/dev start``
#. In a separate tab in the Workbench directory, run ``bin/dev develop-module colwiseproportion``
#. Edit this code; the module will be reloaded in Workbench immediately
