# puppet fix error

exec { 'Fix site':
  command  => 'sudo sed -i "s/.phpp/.php/" /var/www/html/*.php ; sudo service apache2 restart',
  provider => shell,
}