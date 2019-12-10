# Check for file lines in ssh_config

file_line { 'Turn off passwd auth (local)':
  ensure => present,
  path   => '~/.ssh/config',
  line   => 'PasswordAuthentication no',
}

file_line { 'Declare identity file':
  ensure => present,
  path   => '~/.ssh/config',
  line   => 'IdentityFile ~/.ssh/holberton',
}
