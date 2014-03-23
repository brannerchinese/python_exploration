def rule_sequence(s, rules):
    if s == None or len(s) <= 1:
        return s
    s = rules[0](s)
    rules = rules[1:]
    if s:
        return rule_sequence(s, rules)
