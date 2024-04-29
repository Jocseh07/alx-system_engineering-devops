# Install nginx server

exec { 'add_header':
  provider => shell,
  command  => "sudo apt-get -y update ; sudo apt-get -y install nginx ; sudo ufw allow 'Nginx HTTP' ; sed -i \"s/include \/etc\/nginx\/sites-enabled\/\*;/include \/etc\/nginx\/sites-enabled\/\*;\n\tadd_header X-Served-By \"$HOSTNAME\";/\" /etc/nginx/nginx.conf  service nginx restart ;"
}
