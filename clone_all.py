from optparse import OptionParser
import csv
import gitlab
import subprocess
from repo_handler import update_repo
from git import Repo
from keygen import make_key

gl = gitlab.Gitlab.from_config('MMCS', ['./.python-gitlab.cfg'])

def git_clone(url, login):
    subprocess.call(['git', 'clone', url, './submissions/{login}'.format(login)])

def clone_repo(login):
    global gl

    user = gl.users.list(username=login)[0]
    projs = user.projects.list(type='Project')
    for p in projs:
        if 'FIIT' in p.name:
            #print(p.ssh_url_to_repo)
            pass

def sync_repo(login):
    update_repo("./submissions/{}".format(login),
                "git@gitlab.mmcs.sfedu.ru:{}/compilers-fiit.git".format(login),
                login, 'git@gitlab.mmcs.sfedu.ru:mmcs/compilers-fiit.git')

def clone_repos(filename):
    with open(filename, newline='') as csvfile:
        loginreader = csv.reader(csvfile, delimiter=',', quotechar='|')
        for row in loginreader:
            clone_repo(row[0])
            sync_repo(row[0])


if __name__ == "__main__":
    parser = OptionParser()
    parser.add_option("-f", "--file", dest="filename",
                      help="read login list from FILE", metavar="FILE")

    (options, args) = parser.parse_args()

    clone_repos(options.filename)
