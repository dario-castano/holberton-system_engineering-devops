# Configure a nginx server with header

package{'nginx':
  name => 'nginx',
  provider => 'apt',
  ensure => installed
}

exec{'download_conf':
  command => '/usr/bin/wget -q https://raw.githubusercontent.com/dario-castano/holberton-system_engineering-devops/master/0x0F-load_balancer/nginx.conf -O /etc/nginx/nginx.conf',
  require => Package['nginx']
}

service{'nginx_service':
  name => 'nginx',
  enable => 'true',
  ensure => 'running',
  require => [Package['nginx'], Exec['download_conf']]
}

file{'/etc/nginx/nginx.conf':
  notify => Service['nginx_service'],
  require => Package['nginx']
}
