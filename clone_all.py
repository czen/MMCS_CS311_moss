from optparse import OptionParser
import csv
import gitlab
import subprocess
from repo_handler import clone_repo
from git import Repo
from os import path
from keygen import make_key

gl = gitlab.Gitlab.from_config('MMCS', ['./.python-gitlab.cfg'])

#def git_clone(url, login):
#    subprocess.call(['git', 'clone', url, './submissions/{login}'.format(login)])

def clone_repos(filename):
    with open(filename, newline='') as csvfile:
        loginreader = csv.reader(csvfile, delimiter=',', quotechar='|')
        for row in loginreader:
            p = "./submissions/{}".format(row[0])
            if not path.exists(p):
                clone_repo("git@gitlab.mmcs.sfedu.ru:{}/compilers-fiit.git".format(row[0]), p, row[0])


if __name__ == "__main__":
    parser = OptionParser()
    parser.add_option("-f", "--file", dest="filename",
                      help="read login list from FILE", metavar="FILE")

    (options, args) = parser.parse_args()

    clone_repos(options.filename)
