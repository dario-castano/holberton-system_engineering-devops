# Check for file lines in ssh_config

file_line { 'holberton_key':
  ensure => present,
  path   => '~/.ssh/config',
  line   => 'IdentityFile ~/.ssh/holberton',
}

file_line { 'refuse_pass':
  ensure => present,
  path   => '~/.ssh/confg',
  line   => 'PasswordAuthentication no',
}
