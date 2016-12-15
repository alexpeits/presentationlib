presentationlib
===============

Tool for live coding presentations
----------------------------------

**(I will find a better name)**


*presentationlib* is a simple tool for doing presentations via the python REPL.
It was inspired by `these <https://www.youtube.com/watch?v=j6VSAsKAj98>`_
`two <https://www.youtube.com/watch?v=Bm96RqNGbGo>`_ talks by David Beazley.

It can easily present text files, but can also execute python files in the global scope,
so it is the same as the presenter typed in the code or imported it.

The usage is simple, import the ``presentation`` function, declare a mapping to configure the
files that are included in the presentation, and run it.

The mapping can also include a list. Then, multiple uses of it cycle through the options.

Usage
-----

*File structure*::

    |
    |- run_presentation.py
    |- slides/
        |- fib.py
        |- lorem.txt



*run_presentation.py*:

.. code-block:: python

    from presentationlib import presentation

    mapping = {
        'fib': 'fib.py',
        'lorem': {file: 'lorem.txt', wrap: True},
        'test': '~/file.txt',
        'multiple': [
            'fib.py',
            '~/file.txt',
            {'file': 'lorem.txt', 'wrap': True}
        ]
    }

    if __name__ == '__main__':
        presentation(
            mapping, location='slides',
            heading='My Presentation', subheading='waaaaat'
        )


*Presentation*::


    $ python run_presentation.py

    --------------------------------------------------

                 My Presentation                  

    --------------------------------------------------

                     waaaaat                      


    >>> 'hello'
    'hello'
    >>> 'fib'
    +------------------------------------------------------------------------------+
    |                                                                              |
    |  def fibo(lim):                                                              |
    |      a, b = 0, 1                                                             |
    |      while a <= lim:                                                         |
    |          yield a                                                             |
    |          a, b = b, a+b                                                       |
    |                                                                              |
    +------------------------------------------------------------------------------+

    >>> fibo
    <function fibo at 0x7faf003ac500>
    >>> list(fibo(5))
    [0, 1, 1, 2, 3, 5]
    >>>
    >>> 'lorem'
    +------------------------------------------------------------------------------+
    |                                                                              |
    |  Lorem ipsum dolor sit amet, neque voluptatum pede nulla praesent, arcu      |
    |  neque amet sit, cum libero quis gravida arcu, pellentesque amet per amet    |
    |  mi. Justo sapien sit ut, sit arcu lobortis tincidunt, dolor elit lobortis   |
    |  gravida. At at leo egestas est, alias libero nisl nam id, eleifend          |
    |  interdum sagittis congue eiusmod. Rutrum ante rutrum mauris, lorem aliquet  |
    |  placerat sollicitudin alias, tenetur dignissim accusantium elit eros, dui   |
    |  suscipit lacus ut. Wisi sodales exercitationem nullam, non in nunc eget.    |
    |  Sapien eu volutpat felis ac, nibh cursus elit varius.                       |
    |                                                                              |
    +------------------------------------------------------------------------------+

    >>> 'multiple'
    +------------------------------------------------------------------------------+
    |                                                                              |
    |  def fibo(lim):                                                              |
    |      a, b = 0, 1                                                             |
    |      while a <= lim:                                                         |
    |          yield a                                                             |
    |          a, b = b, a+b                                                       |
    |                                                                              |
    +------------------------------------------------------------------------------+

    >>> 'multiple'
    +------------------------------------------------------------------------------+
    |                                                                              |
    |  This is a file                                                              |
    |  Yes, this is a file                                                         |
    |                                                                              |
    +------------------------------------------------------------------------------+

    >>> 'multiple'
    +------------------------------------------------------------------------------+
    |                                                                              |
    |  Lorem ipsum dolor sit amet, neque voluptatum pede nulla praesent, arcu      |
    |  neque amet sit, cum libero quis gravida arcu, pellentesque amet per amet    |
    |  mi. Justo sapien sit ut, sit arcu lobortis tincidunt, dolor elit lobortis   |
    |  gravida. At at leo egestas est, alias libero nisl nam id, eleifend          |
    |  interdum sagittis congue eiusmod. Rutrum ante rutrum mauris, lorem aliquet  |
    |  placerat sollicitudin alias, tenetur dignissim accusantium elit eros, dui   |
    |  suscipit lacus ut. Wisi sodales exercitationem nullam, non in nunc eget.    |
    |  Sapien eu volutpat felis ac, nibh cursus elit varius.                       |
    |                                                                              |
    +------------------------------------------------------------------------------+


Configuration options
---------------------

* ``location``: the directory in which all filenames are searched (except for absolute paths)
* ``use_box``: whether to put text inside an ascii box 
* ``banner``: printed on REPL initialization (a default banner is also provided)
* ``heading`` and ``subheading``: ``banner`` can be a template, these are the template options
