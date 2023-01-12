# Install Nginx package
package { 'nginx':
  ensure => 'installed',
}

# Ensure Nginx service is running
service { 'nginx':
  ensure => 'running',
  enable => true,
}

# Create a default server block configuration
file { '/etc/nginx/sites-available/default':
  ensure => 'file',
  content => '
server {
    listen 80;
    root /var/www/html;
    index index.html;

    location = / {
        return 200 "Hello World!";
    }

    location = /redirect_me {
        return 301 http://www.example.com;
    }

    location / {
        try_files $uri $uri/ =404;
    }
}
',
}

# Enable the default server block configuration
nginx::site { 'default':
  ensure => 'enabled',
