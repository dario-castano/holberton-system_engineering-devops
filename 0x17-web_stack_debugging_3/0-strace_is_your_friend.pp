# fix mispelled wp-locale
exec { 'fix_locale':
  command => '/usr/bin/sudo /bin/sed -i "s/class-wp-locale.phpp/class-wp-locale.php/g" /var/www/html/wp-settings.php',
    }

