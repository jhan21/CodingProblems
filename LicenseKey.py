def licenseKeyFormatting(s: str, k: int) -> str:
    length = len(s)
    rev = ""
    for i in range(length - 1, -1, -1):
        if s[i] != "-":
            if s[i] >= "a" and s[i] <= "z":
                rev += s[i].upper()
            else:
                rev += s[i]

    answer = ""
    hold = ""
    hyphenFlag = False
    for i in range(len(rev)):
        if hyphenFlag == False:
            if len(hold) != k:
                hold += rev[i]
        
            else:
                hold += "-" + rev[i]
                answer += hold
                hyphenFlag = True
                hold = ""
        else:
            if len(hold) != (k - 1):
                hold += rev[i]
            else:
                hold += "-" + rev[i]
                answer += hold
                hold = ""
    answer += hold
    print(answer)
    print(answer[::-1])
    return(answer[::-1])

key = "5F3Z-2e-9-w"
key1 = "2-5g-3-J"
licenseKeyFormatting(key1, 2)
