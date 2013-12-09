def s w,t,p
return p if w==""
[*-1..1].product([*-1..1]).flat_map{|r,c|s w[1..-1],[t[0]+r,t[1]+c],p+[t]} if $g[t]&&["?",$g[t]].include?(w[0])&&!p.include?(t)
end
a,b=ARGF.read.split(/\n\n/)
$g=Hash[*a.split(/\n/).flat_map.with_index{|l,r|l.chars.flat_map.with_index{|e,c|[[r,c],e]}}]
m=b.upcase.scan(/[^,\s]+/).flat_map{|w|$g.keys.flat_map{|t|s w,t,[]}}
puts [$g.group_by{|t,v|t[0]}.sort.map{|e,k|k.map{|t,v|m.include?(t)?v:'.'}.join' '}.join("\n"),"",b]
