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
#   Description:
#       Turn cipherwiki in to a fast, secure and simple to manage
#       personal wiki option.
#


import os
import sys
import urllib
import shutil
import argparse
import webbrowser


global wiki_folder
wiki_folder = "{0}/.cipherwiki/".format(os.getenv('HOME'))


def list_wiki():
    """
    """
    for w in os.listdir(wiki_folder):
        print('[-] {0}'.format(w.strip('.html')))


def new_wiki(wiki_name, wiki_file='empty-cipherwiki-0.02.html'):
    """
    """
    if not os.path.isfile("{0}{1}".format(wiki_folder, wiki_file)):
        sys.stderr.write("[!] Empty wiki file not found, please use --download\n")
        sys.exit(1)

    if os.path.isfile("{0}{1}.html".format(wiki_folder, wiki_name)):
        sys.stderr.write("[!] Wiki file {0} already exists\n".format(wiki_name))
        sys.exit(2)

    shutil.copy("{0}{1}".format(wiki_folder, wiki_file),
                "{0}{1}.html".format(wiki_folder, wiki_name))


def del_wiki(wiki_name):
    """
    """
    if not os.path.isfile("{0}{1}.html".format(wiki_folder, wiki_name)):
        sys.stderr.write("[!] Could not find wiki file {0}\n".format(wiki_name))
        sys.exit(3)

    os.remove("{0}{1}.html".format(wiki_folder, wiki_name))



def download_cipherwiki(target='empty-cipherwiki-0.02.html',
                        source_url=("https://raw.githubusercontent.com"
                                    "/Spacecow99/cipherwiki/master/"
                                    "empty-cipherwiki-0.02.html")):
    """
    Download a new copy of cipherwiki from github
    """
    try:
        with open("{0}{1}".format(wiki_folder, target), 'w') as f:
            source = urllib.urlopen(source_url)
            f.write(source.read())
        print("[+] Download successful, file saved to {0}.".format(target))
    except():
        sys.stderr.write('[!] Could not download cipherwiki source file.\n')
        sys.exit(4)


def main():
    parser = argparse.ArgumentParser(prog='cipherwiki-cli',
                                     description=("CLI tool for managing "
                                     "multiple cipherwiki pages "
                                     "for multiple topics."))
    parser.add_argument('-w', '--wiki', metavar='WIKI', type=str,
                        action='store', nargs='+',
                        help='Open wiki(s) for editing in the web browser')
    parser.add_argument('-l', '--list', action='store_true',
                        help='List all available wikis')
    parser.add_argument('-n', '--new', metavar='WIKI', action='store',
                        help='Create a new empty wiki file')
    parser.add_argument('-r', '--remove', metavar='WIKI', action='store',
                        help='Delete specified wiki file')
    parser.add_argument('-d', '--download', action='store_true',
                        help='Download a new copy of cipherwiki from github')
    parser.add_argument('-v', '--version', action='version',
                        version='Cipherwiki-CLI 0.4')
    args = parser.parse_args()

    # Setup cipherwiki folder under ~/.cipherwiki
    if not os.path.isdir(wiki_folder):
        sys.stderr.write("[+] Creating cipherwiki folder in '{0}'.\n".format(wiki_folder))
        os.mkdir(wiki_folder)
        download_cipherwiki()

    if args.download:
        download_cipherwiki()

    if args.list:
        list_wiki()
    elif args.new:
        new_wiki(args.new)
    elif args.remove:
        del_wiki(args.remove)
    else:
        for wiki in args.wiki:
            if os.path.isfile("{0}{1}.html".format(wiki_folder, wiki)):
                webbrowser.open_new_tab("file://{0}{1}.html".format(wiki_folder, wiki))
            else:
                sys.stderr.write("[!] Could not find the wiki {0}\n".format(wiki))


if __name__ == '__main__':
    try:
        main()
    except(KeyboardInterrupt):
        print()
