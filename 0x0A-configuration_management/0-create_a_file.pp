# create file named school in tmp with content and ownership chamge
file {'/tmp/school':
        path    => file,
        content => 'I love Puppet',
        mode    => '0744'
        group   => 'www-data',
        owner   => 'www-data'
}
