import gitlab

gl = gitlab.Gitlab.from_config('MMCS', ['./.python-gitlab.cfg'])

user = gl.users.list(username='ev')[0]

k = user.keys.create(
    {
       'title': 'test_key',
       'key': open('./keys/ev.id_rsa.pub').read()
    }
)

