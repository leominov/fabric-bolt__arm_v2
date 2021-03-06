from fabric.api import *
from arm_v2.params import yii2, system
from arm_v2.language import messages
from arm_v2.procedure import *


def init():
    env.folder = system['project'].format(env.ROOT_PATH, env.ALIAS)
    print 'Alias: {0}\nBranch: {1}\n'.format(env.ALIAS, env.BRANCH)


@task
def delete():
    """Delete ARM"""
    init()

    if not has_space(env.ALIAS):
        print messages['nothing']
        return False

    # Remove folder
    run(system['rm'].format(env.folder))


@task
def update():
    """Create or update ARM"""
    init()

    if has_space(env.ALIAS):
        print messages['nothing']
        checkout_repo(env.BRANCH)
    else:
        # Make folder
        run(system['md'].format(env.folder))

        # Clone repository
        state = clone_repo(env.REPO, env.BRANCH)
        if not state:
            print messages['branch_error']
            return False

    vendor_install()

    print yii2['host'].format(env.ALIAS, env.host)
