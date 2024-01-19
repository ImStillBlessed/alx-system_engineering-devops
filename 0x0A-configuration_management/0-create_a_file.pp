file {'0-create_a_file.pp':
	path => /tmp/school,
	group => www-data,
	owner => www-data,
	content => "I love Puppet",
	mode => 0744
}
