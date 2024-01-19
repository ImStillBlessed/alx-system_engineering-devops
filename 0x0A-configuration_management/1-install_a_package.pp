# installs flask in the system
package {'flask':
	ensure => '2.1.0',
	provider => 'pip3'
}
