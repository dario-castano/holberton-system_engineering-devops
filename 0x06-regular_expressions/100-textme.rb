#!/usr/bin/env ruby
puts ARGV[0].scan(/\[from:(\+\w+|\w+)\] \[to:(\+\w+|\w+)\] \[flags:([:0-9-]+)\]/).join(", ")
