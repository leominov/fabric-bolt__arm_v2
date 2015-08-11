composer = {
    'download': 'curl -sS https://getcomposer.org/installer | {0}',
    'file': 'composer.phar',
    'install': '{0} {1} install',
}

git = {
    'pull': 'git pull',
    'clone': 'git clone {0} ./',
    'checkout': 'git checkout {0}',
    'branch': 'git branch -a | grep \'{0}\' | wc -l',
    'commit_file': 'git log -1 --format="build date: $(date)%ncommit: %h @ %cD (%ar)%nauthor: %an <%ae>%nsubject: %s" > frontend/web/commit.txt',
}

yii2 = {
    'init': '{0} init --env=Development --overwrite=All',
    'host': 'http://{0}.{1}/',
}

system = {
    'project': '{0}/{1}/',
    'php': 'php',
    'rm': 'rm -Rf {0}',
    'md': 'mkdir {0}',
}
