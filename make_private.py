from optparse import OptionParser
import csv
import gitlab

gl = gitlab.Gitlab.from_config('MMCS', ['./.python-gitlab.cfg'])

def make_private_repo(login):
    global gl

    user = gl.users.list(username=login)[0]
    projs = user.projects.list(type='Project')
    for p in projs:
        if 'FIIT' in p.name:
            from gitlab.v4.objects import UserProject
            from gitlab.v4.objects import UserProjectManager
            #print(p.manager)
            p.attributes['visibility'] = 'private'
            gl.projects.update(p.get_id(), p.attributes)





def make_private_repos(filename):
    with open(filename, newline='') as csvfile:
        loginreader = csv.reader(csvfile, delimiter=',', quotechar='|')
        for row in loginreader:
            make_private_repo(row[0])


if __name__ == "__main__":
    parser = OptionParser()
    parser.add_option("-f", "--file", dest="filename",
                      help="read login list from FILE", metavar="FILE")

    (options, args) = parser.parse_args()

    make_private_repos(options.filename)
