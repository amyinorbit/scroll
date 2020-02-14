"""
Scroll version 2020.2r1 (Feb 14 2020)
Copyright (c) 2020 Amy Parent <amy@amyparent.com>

Usage: scroll [options] <command> [<args>...]

\u001b[1mOptions\u001b[0m
    -h, --help      Print this help message and exit

\u001b[1mCommands\u001b[0m
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
from . import commands

COMMANDS = {
    'list': commands.list_cmd,
    'config': commands.config_cmd
}

def main():
    args = docopt(__doc__, version='0.1.1rc', options_first=True)

    cmd = args['<command>']
    cmd_args = [cmd] + args['<args>']

    if cmd in COMMANDS:
        COMMANDS[cmd].run(cmd_args)
    else:
        exit(f'{cmd} is not a scroll command. See \'scroll --help\'.')