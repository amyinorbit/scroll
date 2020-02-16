import os.path as path

class OptionsObj(object):
    def __init__(self, **kwargs):
        for (k, v) in kwargs.items():
            setattr(self, k, v)

    def __repr__(self):
        return f'{self.__dict__}'

def get_rc_path():
    return path.expanduser('~/.scrollrc')

def get_default_db():
    return path.expanduser('~/.scroll')

DEFAULTS = OptionsObj(
    path=get_default_db(),
    verbose=True,
    max_authors=2,
    title_length=60
)

def load_options():
    return DEFAULTS
