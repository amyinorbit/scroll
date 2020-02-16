"""
Access and edit scroll's configuration.

Usage: scroll config --get NAME
       scroll config --set NAME VALUE
       scroll config

Options
    -g NAME, --get NAME     Print value for a configuration key
    -s NAME, --set NAME     Set value for a configuration key
    -h, --help              Show this help message

"""
from docopt import docopt

def run(args, conf):
    args = docopt(__doc__, argv=args)
    print(args)

