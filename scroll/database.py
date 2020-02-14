import os.path
import sys
import re
import biblib
from biblib import algo
from biblib import bib
from colorama import Fore, Back, Style
from . import options

mathmode = re.compile(r'(?<!\\)\$')

def sanitize_latex(string):
    return re.sub(mathmode, r'\$', string)

class Formatter(object):

    def __init__(self, conf):
        self.conf = conf

    def format(self, entry):
        return f'[{Fore.MAGENTA}{entry.key}{Style.RESET_ALL}] ' \
             + f'{Style.BRIGHT}{self.__authors(entry)}{Style.RESET_ALL}' \
             + f'{self.__title(entry)}' \
             + f'{Style.BRIGHT}{self.__year(entry)}{Style.RESET_ALL}'

    def __authors_et_al(self, names):
        if not len(names):
            return ''
        if len(names) >= self.conf.max_authors:
            return '%s et al. ' % names[0]
        elif len(names) > 1:
            return '%s and %s. ' % (', '.join(names[:-1]), names[-1])
        else:
            return names[0] + '. '

    def __authors(self, entry):
        if not 'author' in entry:
            return ''
        authors = [self.__filters(a.pretty()) for a in entry.authors()]
        return self.__authors_et_al(authors)

    def __title(self, entry):
        if not 'title' in entry:
            return ''
        title = entry['title'] # self.__filters(sanitize_latex(entry['title']))
        if len(title) > self.conf.title_length:
            return '"%s..."' % title[:self.conf.title_length]
        return '"%s" ' % title

    def __year(self, entry):
        if not 'year' in entry:
            return ''
        return '(%s)' % entry['year']

    def __filters(self, title):
        return algo.tex_to_unicode(title)

def load(conf):
    try:
        with open(os.path.join(conf.path, 'refs.bib'), 'r') as in_file:
            return bib.Parser().parse(in_file, log_fp=sys.stderr).get_entries()
    except IOError as ioe:
        return {}
    except Exception as e:
        raise e
