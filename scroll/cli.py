"""
Scroll version 2020.2r1 (Feb 14 2020)
Copyright (c) 2020 Amy Parent <amy@amyparent.com>

Usage:
    scroll [options] COMMAND [ARGS...]

Options:
    -h, --help      Print this help message and exit

Commands:
    list            Query the bibliography
    add             Add an entry to the bibliography
    remove          Remove an entry from the bibliography
    export          Export the bibliography for external usage
    config          Configure scroll


Report bugs to: amy@amyparent.com
scroll home page: <https://github.com/amyinorbit/scroll>

"""
from docopt import docopt
import sys
import colorama
from . import commands
from . import options


COMMANDS = {
    'list': commands.list_cmd,
    'config': commands.config_cmd
}

def main():
    colorama.init()
    conf = options.load_options()
    args = docopt(__doc__, version='0.1.1rc', options_first=True)

    cmd = args['COMMAND']
    cmd_args = [cmd] + args['ARGS']


    if cmd in COMMANDS:
        COMMANDS[cmd].run(cmd_args, conf)
    else:
        exit(f'{cmd} is not a scroll command. See \'scroll --help\'.')
