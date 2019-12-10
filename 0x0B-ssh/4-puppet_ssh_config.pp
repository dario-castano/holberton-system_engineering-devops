# Check for file lines in ssh_config

file_line { 'Turn off passwd auth':
  ensure => present,
  path   => '~/.ssh/confg',
  line   => 'PasswordAuthentication no',
}

file_line { 'Declare identity file':
  ensure => present,
  path   => '~/.ssh/config',
  line   => 'IdentityFile ~/.ssh/holberton',
}
