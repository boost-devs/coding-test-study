# String
# Problem: 4650
# Memory: 29200KB
# Time: 76ms

mo = "aeiou"
s = ""

s = input()
while not (s == "end"):
    acc = True
    ja_ = 0
    mo_ = 0
    mo_find = False

    s = s + ' '

    for i in range(len(s)-1):
        if s[i] == s[i + 1]:
            if s[i] != 'e' and s[i] != 'o':
                acc = False
                break

        if s[i] in mo:
            mo_find = True
            if mo_ >= 2:
                acc = False
                break
            else:
                mo_ += 1
                ja_ = 0
        else:
            if ja_ >= 2:
                acc = False
                break
            else:
                ja_ += 1
                mo_ = 0

    if mo_find == False:
        acc = False

    if acc == False:
        print(f'<{s[:-1]}> is not acceptable.')
    else:
        print(f'<{s[:-1]}> is acceptable.')

    s = input()

