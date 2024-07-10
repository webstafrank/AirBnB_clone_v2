#!/usr/bin/env bash
# Script to set up web servers for the deployment of web_static

# Install Nginx if it is not already installed
if ! dpkg -l | grep -qw nginx; then
    sudo apt-get update
    sudo apt-get install -y nginx
fi

# Create necessary directories
sudo mkdir -p /data/web_static/releases/test /data/web_static/shared

# Create a fake HTML file
echo "<html>
  <head>
  </head>
  <body>
    Holberton School
  </body>
</html>" | sudo tee /data/web_static/releases/test/index.html

# Creating symbolic link
sudo ln -sf /data/web_static/releases/test/ /data/web_static/current

# Giving ownership of the /data/ folder to the ubuntu user and group
sudo chown -R ubuntu:ubuntu /data/

# Update Nginx configuration to serve the content
nginx_config="server {
    listen 80 default_server;
    listen [::]:80 default_server;

    root /var/www/html;
    index index.html index.htm;

    server_name _;

    location /hbnb_static {
        alias /data/web_static/current;
    }

    location / {
        try_files \$uri \$uri/ =404;
    }
}"

echo "$nginx_config" | sudo tee /etc/nginx/sites-available/default

# Restart Nginx to apply the changes
sudo service nginx restart

exit 0
