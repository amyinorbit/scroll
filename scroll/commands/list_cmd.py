"""
Usage:
    scroll list [-h] | [--cite-key] [QUERY...]

Options:
    -k, --cite-key  Print only the cite keys of matching get_entries
    -h, --help      Print this help message and exit

"""
import argparse
from docopt import docopt
from .. import database
import biblib
from biblib import messages

def run(args, conf):
    opt = docopt(__doc__, argv=args)

    try:
        db = database.load(conf)
        f = database.Formatter(conf)

        for entry in db.values():
            print(f.format(entry))

    except biblib.messages.InputError as e:
        exit(f'Input error: {e.args}')
    except Exception as e:
        # raise e
        print(f'Fatal error: {e}')
        raise e
