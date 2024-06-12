# fix high number of requests

exec { 'hard-nofile':
    provider => shell,
    command  => 'sudo sed -i "s/nofile 5/nofile 1000000/" /etc/security/limits.conf',
    before   => Exec['soft-nofile'],
}
exec { 'soft-nofile':
    provider => shell,
    command  => 'sudo sed -i "s/nofile 4/nofile 1000000/" /etc/security/limits.conf',
}