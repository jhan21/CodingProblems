def splitString(s):

    splitsList = []

    for i in range(len(s) - 1):
        a = s[:i+1]
        for j in range(i+1,len(s) - 1):
            b = s[i+1:j+1]
            c = s[j+1:len(s)]
            splitsList.append([a,b,c])
    print(splitsList)
    return 0

splitString("xzxzx")