"""
Usage: scroll [options] <command> [<args>...]

\u001b[1mOptions\u001b[0m
    -h, --help      Print this help message and exit

\u001b[1mCommands\u001b[0m
    list            Query the bibliography
    add             Add an entry to the bibliography
    remove          Remove an entry from the bibliography
    export          Export the bibliography for external usage
    config          Configure scroll
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