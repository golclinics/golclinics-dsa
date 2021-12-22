def wild_card_matching(s, p):
    n = len(s)

    if n == 1 and s[0] == "*":
        return True

    for i in range(n):
        if(len(p) > i):
            if s[i] != p[i] and p[i] != "?" and p[i] != "*":
                return False
            if p[i] == "*" and i == len(p) - 1:
                return True

    if len(s) != len(p):
        return False

    return True

s = "acdcb"
p = "a*c?b"
print(wild_card_matching(s, p))