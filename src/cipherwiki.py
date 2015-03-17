#!/usr/bin/env python
#
#   cipherwiki-cli - cipherwiki.py
#
#   CLI tool for managing multiple cipherwiki pages/installations
#   for multiple topics. 
#
#   Author: Spacecow
#   Title: Cipherwiki-CLI
#   Date: 15/03/15
#   Description: This script makes cipherwiki a fast, simple, secure and easy to manage personal wiki option.
#
#

import os
import sys
import urllib
import shutil
import os.path
import argparse
import webbrowser
import ConfigParser


def list_wiki(wiki_folder):
    """"""
    pass


def new_wiki(wiki_name, wiki_file, wiki_folder):
    """"""
    pass


def del_wiki(wiki_name, wiki_folder):
    """"""
    pass


def download_cipherwiki(target='empty-cipherwiki-0.02.html'):
    """Download a new copy of cipherwiki from github"""
    raw_source = "https://raw.githubusercontent.com/felipedaragon/cipherwiki/master/empty-cipherwiki-0.02.html"
    try:
        source = urllib.urlopen(raw_source)
    except():
        sys.stderr.write('[!] Could not download cipherwiki source file.\n')
        sys.exit(3)
    with open(target, 'w') as f:
        f.write(source.read())
    print("[*] Download successful, file saved to {0}.".format(target))


def build_config(target='cipherwiki.cfg'):
    """Create and write a new configuration file"""
    config = ConfigParser.SafeConfigParser()
    config.add_section('CIPHERWIKI')
    config.set('CIPHERWIKI', 'WIKI_FOLDER', '{0}/.cipherwiki/'.format(os.getenv('HOME')))
    config.set('CIPHERWIKI', 'WIKI_FILE', 'empty-cipherwiki-0.02.html')
    config.set('CIPHERWIKI', 'WIKI_EXAMPLE', 'true')


def main():
    parser = argparse.ArgumentParser(prog='cipherwiki', description='CLI tool for managing multiple cipherwiki pages for multiple topics.')
    parser.add_argument('wikis', metavar='WIKI', type=str, action='store', nargs='+', help='')
    parser.add_argument('-l', '--list', action='store_true', help='')
    parser.add_argument('-n', '--new', metavar='WIKI', action='store', help='')
    parser.add_argument('-r', '--remove', metavar='WIKI', action='store', help='')
    parser.add_argument('-c', '--configuration', metavar='PATH', action='store', help='Create a default config file')
    parser.add_argument('-d', '--download', metavar='PATH', action='store', help='Download a new copy of cipherwiki from github')
    parser.add_argument('-v', '--version', action='store_true', help='Print cipherwiki version information')  #replace with builtin argparse version type
    args = parser.parse_args()

 
if __name__ == '__main__':
    try:
        main()
    except(KeyboardInterrupt):
        print()