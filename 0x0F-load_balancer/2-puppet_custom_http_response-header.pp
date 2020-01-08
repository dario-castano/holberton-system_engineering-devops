# Configure a nginx server with header

exec{'update_install_apt':
  command => "sudo apt-get update && sudo apt-get install -y nginx"
}

exec{'download_conf':
  command => "/usr/bin/wget -q https://raw.githubusercontent.com/dario-castano/holberton-system_engineering-devops/master/0x0F-load_balancer/nginx.conf -O /etc/nginx/nginx.conf",
  creates => "/etc/nginx/nginx.conf",
}

file{'/etc/nginx/nginx.conf':
  mode => 0755,
  require => Exec["download_conf"],
}

exec{'start_nginx':
  command => "sudo service nginx start"
}
