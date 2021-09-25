import git
import os

def get_key(login):
    git_ssh_identity_file = os.path.expanduser('./keys/{}/private.key'.format(login))
    git_ssh_cmd = 'ssh -i %s' % git_ssh_identity_file
    return git_ssh_cmd

def clone_repo(git_url, path, login):
    with git.Git().custom_environment(GIT_SSH_COMMAND=get_key(login)):
        r = git.Repo.clone_from(git_url, path, branch='master')

    # empty_repo = git.Repo.init(path)
    # origin = empty_repo.create_remote('origin', git_url)
    # origin.fetch()  # assure we actually have data. fetch() returns useful information
    # # Setup a local tracking branch of a remote branch
    # empty_repo.create_head('master', origin.refs.master)  # create local branch "master" from remote "master"
    # empty_repo.heads.master.set_tracking_branch(origin.refs.master)  # set local "master" to track remote "master
    # empty_repo.heads.master.checkout()  # checkout local "master" to working tree
    # # push and pull behaves similarly to `git push|pull`
    # origin.pull()
    # origin.push()

def update_from_upstream(path, login, upstream_url):
    with git.Git().custom_environment(GIT_SSH_COMMAND=get_key(login)):
        r = git.Repo(path)
        r.heads.master.checkout()
        u = r.create_remote('upstream', upstream_url)
        u.fetch()
        #master = r.heads.master
        m = r.git.merge('upstream/master')
        r.remotes.origin.push()

def update_repo(path, url, login, upstream_url):
    clone_repo(url, path, login)
    update_from_upstream(path, login, upstream_url)


if __name__ == "__main__":
    # clone_repo("git@gitlab.mmcs.sfedu.ru:ev/compilers-fiit.git", "./submissions/ev", 'ev')
    # update_from_upstream("./submissions/ev", 'ev', 'git@gitlab.mmcs.sfedu.ru:mmcs/compilers-fiit.git')
    #clone_repo("git@gitlab.mmcs.sfedu.ru:veraverina/compilers-fiit.git", "./submissions/veraverina", 'veraverina')
    #update_from_upstream("./submissions/veraverina", 'veraverina', 'git@gitlab.mmcs.sfedu.ru:mmcs/compilers-fiit.git')
    pass
