from __future__ import print_function

import os
import sys
import code
import inspect
from textwrap import fill
from itertools import cycle

from .utils import boxify, is_generator, container
from . import config


CLEAR_SCR = '\033c'

old_displayhook = sys.displayhook


class mod_displayhook(object):

    def __init__(self, mapping, location, use_box, box_width):
        self.mapping = mapping
        self.location = location
        self.use_box = use_box
        self.box_width = box_width
        self.text_width = box_width - 6

    def resolve(self, fn):
        if os.path.isabs(fn):
            return fn
        local = os.path.join(self.location, fn)
        if os.path.exists(local):
            return local
        return ''

    def __call__(self, obj):
        globals_ = inspect.stack()[1][0].f_globals
        wrap = False
        try:
            # may raise TypeError, goes to except ...
            item = self.mapping.get(obj)
            if item is None:
                # ... as well as this
                raise TypeError
        except TypeError:
            old_displayhook(obj)
            return

        if is_generator(item):
            try:
                item = next(item)
            except StopIteration:
                return

        if isinstance(item, dict):
            wrap = item.get('wrap', False)
            fn = item.get('file')
        else:
            fn = item

        fp = self.resolve(fn)

        if fp:
            with open(fp, 'r') as f:
                text = f.read()
            if fn.rstrip('/').endswith('.py'):
                exec(text, globals_, globals_)
            if wrap:
                text = fill(text, config.TEXT_WIDTH)
            print(CLEAR_SCR)
            if self.use_box:
                print(boxify(text, width=self.box_width))
            else:
                print(text)
            print()
        else:
            old_displayhook(obj)


def presentation(
        mapping, location=None, use_box=True, box_width=config.BOX_WIDTH,
        banner=None, heading=None, subheading=None):

    slides = dict()

    for k, v in mapping.items():
        if isinstance(v, container):
            slides[k] = cycle(v)
        else:
            slides[k] = v

    if location is None:
        frame = sys._getframe()
        location = os.path.dirname(frame.f_back.f_code.co_filename)

    location = os.path.abspath(location)

    sys.displayhook = mod_displayhook(slides, location, use_box, box_width)

    if banner is None:
        banner = config.BANNER_TEMPLATE
    if heading is None:
        heading = config.HEADING
    if subheading is None:
        subheading = config.SUBHEADING

    code.interact(
        banner=banner.format(heading=heading, subheading=subheading),
        local=locals()
    )
