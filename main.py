def check(string):
    my_string = string.lower()
    vowels = set("aeiou")
    s = set({})
    for char in my_string:
        if char in vowels:
            s.add(char)
        else:
            pass
    if len(s) == len(vowels):
        print("Accepted")
    else:
        print("Not Accepted")
string = "EIO Suman"
check(string)