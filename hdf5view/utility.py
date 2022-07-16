import os
from functools import partial


def relative_path_convert(x, fp=None):
    if fp is None:
        fp = __file__
    return os.path.abspath(os.path.join(os.path.split(fp)[0], x))


resource_path = partial(os.path.join, os.path.join(relative_path_convert('.'), 'resources'))

