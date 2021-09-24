import gitlab

gl = gitlab.Gitlab.from_config('MMCS', ['./.python-gitlab.cfg'])

projects = gl.projects.list()
for project in projects:
    print(project)

