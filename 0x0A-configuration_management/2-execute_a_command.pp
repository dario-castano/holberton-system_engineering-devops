# Kill a process using exec

exec { 'pkill killmenow':
  command => 'pkill killmenow',
  path    => '/usr/bin',
}
