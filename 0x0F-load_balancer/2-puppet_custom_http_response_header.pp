# Install nginx server

exec { 'install':
  provider => shell,
  command  => "sudo apt-get -y update ; sudo apt-get -y install nginx ; sudo ufw allow 'Nginx HTTP' ; sudo echo 'Hello World!' >/var/www/html/index.nginx-debian.html ; sudo echo -e 'server {\n    listen 80 default_server;\n	  listen [::]:80 default_server;\n    root /var/www/html;\n	  index index.html index.htm index.nginx-debian.html;\n    server_name _;\n    location / {\n		try_files \$uri \$uri/ =404;\n	}\n    if ( \$request_filename ~ redirect_me ) {\n        rewrite ^ https://www.youtube.com/watch?v=QH2-TGUlwu4 permanent;\n    }\n}' >/etc/nginx/sites-enabled/default ; service nginx restart ; sudo sed -i \"s/include \/etc\/nginx\/sites-enabled\/\*;/include \/etc\/nginx\/sites-enabled\/\*;\n\tadd_header X-Served-By \"$HOSTNAME\";/\" /etc/nginx/nginx.conf ; sudo service nginx restart"
}
