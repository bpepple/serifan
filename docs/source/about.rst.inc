**serifan** is a python wrapper for the Shortboxed API.

.. code-block:: python

    import serifan

    sb = serifan.api()

    # Get this weeks comic releases.
    results = sb.new_releases()

    # Print the results
    for i in results:
        print(f"{i.title}")


Get It Now
==========


.. code-block:: bash

    $ pip3 install --user serifan