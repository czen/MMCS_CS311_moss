from optparse import OptionParser
import csv
import gitlab
from keygen import make_key

gl = gitlab.Gitlab.from_config('MMCS', ['./.python-gitlab.cfg'])

def setup_user_key(login):
    global gl

    user = gl.users.list(username=login)[0]
    make_key(login)

    k = user.keys.create(
        {
            'title': 'admin_key',
            'key': open('./keys/{}/public.key'.format(login)).read()
        }
    )

def setup_users_key(filename):
    with open(filename, newline='') as csvfile:
        loginreader = csv.reader(csvfile, delimiter=',', quotechar='|')
        for row in loginreader:
            setup_user_key(row[0])


if __name__ == "__main__":
    parser = OptionParser()
    parser.add_option("-f", "--file", dest="filename",
                      help="read login list from FILE", metavar="FILE")

    (options, args) = parser.parse_args()

    setup_users_key(options.filename)
