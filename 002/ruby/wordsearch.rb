def search(grid, rc, word, path)
  return path if word == ""
  return [] if path.include?(rc) || !["?", grid[rc]].include?(word[0])
  [*-1..1].product([*-1..1]).flat_map {|r,c|
    search(grid, [rc[0]+r,rc[1]+c], word[1..-1], path + [rc])
  }
end

grid_s, word_s = ARGF.read.upcase.split(/\n\n/)
gridline = grid_s.split(/\n/).map.with_index {|line,row|
  line.chars.map.with_index {|ch,col| [[row,col],ch] }
}
grid = Hash[*gridline.flatten(2)]

mark = word_s.split(/,/).flat_map {|word|
  grid.keys.flat_map {|rc| search(grid, rc, word.strip, [])}
}

puts [gridline.map {|rowline|
  rowline.map {|rc, ch| mark.include?(rc) ? ch : '.' }.join(" ")
}.join("\n"), nil, word_s]
