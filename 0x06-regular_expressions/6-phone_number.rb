#!/usr/bin/env ruby
# A regexp that matches a regular pattern of phone number
puts ARGV[0].scan(/^\d{10}$/).join
