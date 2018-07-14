def fix_2nd(s):
    if len(s) < 2: return s
    s2 = s.replace(s[1], "*")
    return s2[0] + s[1] + s2[2:]

print(fix_2nd("eel"))
print(fix_2nd("gooooogle"))
print(fix_2nd("apple"))
print(fix_2nd("orange"))
print(fix_2nd("i"))


