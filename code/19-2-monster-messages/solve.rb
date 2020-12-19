#!/usr/bin/env ruby
rx31 = '(?:b(?:b(?:aba|baa)|a(?:b(?:ab|(?:a|b)a)|a(?:ba|ab)))|a(?:b(?:(?:ab|(?:a|b)a)b|(?:(?:a|b)a|bb)a)|a(?:bab|(?:ba|bb)a)))'
rx42 = '(?:(?:b(?:a(?:bb|ab)|b(?:a|b)(?:a|b))|a(?:bbb|a(?:bb|a(?:a|b))))b|(?:(?:(?:aa|ab)a|bbb)b|(?:(?:a|b)a|bb)aa)a)'

rx8 = "#{rx42}+?"
rx11 = "(#{rx42}\\g<1>*#{rx31})"
rx0 = "^#{rx8}#{rx11}$"
puts(rx0)
rx0 = Regexp.new(rx0)

sample = <<~EOL
abbbbbabbbaaaababbaabbbbabababbbabbbbbbabaaaa
bbabbbbaabaabba
babbbbaabbbbbabbbbbbaabaaabaaa
aaabbbbbbaaaabaababaabababbabaaabbababababaaa
bbbbbbbaaaabbbbaaabbabaaa
bbbababbbbaaaaaaaabbababaaababaabab
ababaaaaaabaaab
ababaaaaabbbaba
baabbaaaabbaaaababbaababb
abbbbabbbbaaaababbbbbbaaaababb
aaaaabbaabaaaaababaa
aaaabbaaaabbaaa
aaaabbaabbaaaaaaabbbabbbaaabbaabaaa
babaaabbbaaabaababbaabababaaab
aabbbbbaabbbaaaaaabbbbbababaaaaabbaaabba
EOL

res = sample.chomp.lines.map {|s| rx0.match?(s.chomp) ? 1 : 0 }.sum
puts(res)
