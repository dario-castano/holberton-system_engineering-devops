# Check for file lines in ssh_config

file_line { 'holberton_key':
  ensure => present,
  path   => '~/.ssh/config',
  line   => 'IdentityFile ~/.ssh/holberton',
}

file_line { 'check_no_pass_auth':
  ensure => absent,
  path   => '~/.ssh/confg',
  line   => 'PasswordAuthentication yes',
}
