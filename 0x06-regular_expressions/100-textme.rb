#!/usr/bin/env ruby
puts ARGV[0].scan(/\[from:(\+\w+|\w+)\] \[to:([\+0-9]+)\] \[flags:([:0-9-]+)\]/).join(", ")