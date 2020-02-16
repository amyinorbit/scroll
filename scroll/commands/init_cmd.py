"""
Create a new scroll database

Usage: scroll init [PATH]

Arguments
    PATH                    The path to the new database.

Options
    -h, --help              Print this help message and exit.

"""
import argparse
from docopt import docopt
import os.path as path
from os import mkdir
from .. import options

def run(args, conf):
    opt = docopt(__doc__, argv=args)
    try:
        dbp = path.abspath(opt['PATH']) if opt['PATH'] else options.get_default_db()
        if path.exists(dbp):
            print(f'`{dbp}\' already exists')
        else:
            mkdir(dbp, 0o755)
            print(f'New database created at `{dbp}\'')

    except OSError as e:
        exit(f'File system error: {e}')
