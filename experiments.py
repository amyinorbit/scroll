#!/usr/bin/env python3
import requests
import biblib
from biblib import bib
from biblib import algo
from colorama import Fore, Back, Style
import sys

def author_pretty(names):
    if not len(names):
        return ''
    if len(names) >= 4:
        return '%s et al.' % names[0]
    elif len(names) > 1:
        return '%s and %s' % (', '.join(names[:-1]), names[-1])
    else:
        return names[0]

def get_authors(entry):
    return [algo.tex_to_unicode(a.pretty()) for a in entry.authors()]

def author_filter(value):
    def predicate(entry):
        return value in ' '.join(get_authors(entry))
    return predicate


try:

    QUERY = 'Helling'


    with open('refs.bib', 'r') as bib:
        db = biblib.bib.Parser().parse(bib, log_fp=sys.stderr).get_entries()
    # biblib.bib.resolve_crossrefs(db)
    for v in filter(author_filter(QUERY), db.values()):
        print(f'{Fore.MAGENTA}{Style.BRIGHT}{v.key}{Style.RESET_ALL}')
        print(f'\t{author_pretty(get_authors(v))}')
        print('\t%s' % v['title'])
except biblib.messages.InputError:
    sys.exit(1)
