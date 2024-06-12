# fix high number of requests

exec { 'limit':
    provider => shell,
    command  => 'sudo echo "ULIMIT=\"-n 4096\"" > /etc/default/nginx',
    before   => Exec['restart-nginx'],
}
exec { 'restart-nginx':
    provider => shell,
    command  => 'sudo service nginx restart',
}