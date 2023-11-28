#!/usr/bin/env ruby
# Ruby script that accepts one argument
# and pass it to a regular expression matching method

if ARGV.empty?
  puts "Usage: #{$PROGRAM_NAME} <string>"
else
  input = ARGV[0]
  pattern = /School/

  if match_data = input.match(pattern)
    puts match_data[0]
  else
    puts
  end
end

