from fabric.api import cd, run, env
from fabric.contrib.files import exists
from language import messages
from params import git, system, composer, yii2


def has_space(alias):
    if not exists(env.folder):
        print messages['space_not_exists'].format(env.folder)
        return False

    print messages['space_exists'].format(alias)
    return True


def has_branch(branch):
    with cd(env.folder):
        result = run(git['branch'].format(branch))
        counter = int(result.strip())

        if counter:
            return True

    return False


def vendor_install():
    with cd(env.folder):
        run(composer['download'].format(system['php']))
        run(composer['install'].format(system['php'], composer['file']))
        run(yii2['init'].format(system['php']))


def checkout_repo(branch):
    with cd(env.folder):
        run(git['pull'])
        run(git['checkout'].format(branch))
        run(git['commit_file'])
        vendor_install()


def clone_repo(repo, branch):
    with cd(env.folder):
        run(git['clone'].format(repo))

        if not has_branch(branch):
            run(system['rm'].format(env.folder))
            return False

    return True
