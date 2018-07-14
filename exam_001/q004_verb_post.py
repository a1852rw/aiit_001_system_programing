def verb_post(s):
    irregular = {
        "go": "went", 
        "put": "put", 
        "write": "wrote", 
        "find": "found",
        "read": "read",
        }
    if s in irregular: 
        return irregular[s]
    if s[-1] == "c":
        return s + "ked"
    if s[-1] == "e":
        return s + "d"
    if s[-1] == "y" and not s[-2] in ["a", "i", "u", "e", "o"]:
        return s[:-1] + "ied"
    return s + "ed"

print(verb_post("play"))
print(verb_post("like"))
print(verb_post("try"))
print(verb_post("picnic"))
print(verb_post("write"))
print(verb_post("go"))
print(verb_post("read"))

