
class OptionsObj(object):
    def __init__(self, **kwargs):
        for (k, v) in kwargs.items():
            setattr(self, k, v)

    def __repr__(self):
        return f'{self.__dict__}'

DEFAULTS = OptionsObj(
    path='/home/amy/scrolldb',
    verbose=True,
    max_authors=2,
    title_length=60
)

def load_options():
    return DEFAULTS
