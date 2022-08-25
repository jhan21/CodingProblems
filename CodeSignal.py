def codedoc(s):
    
    hashMap = {}
    hashSet = set()
    addWord = ""
    palindromeFlag = True

    
    for i in range(len(s)):
        addWord = addWord + s[i]
        for j in range(len(addWord)//2):
            if addWord[i] != addWord[len(addWord) - 1 - j]:
                palindromeFlag = False

        if palindromeFlag:
            hashSet.add(addWord)
    longestPali = ""
    print(hashSet)
    for pali in hashSet:
        if len(longestPali) < len(pali):
            longestPali = pali
    print(longestPali)
    print(len(longestPali), len(s))
    answer = s[len(longestPali):len(s)]

    print(answer)
    
    return answer

def codedoc2(string):
    answer = string
    wordSet = set()
    wordSet.add("test")
    hold = ""
    while len(answer) > 1 and len(wordSet) > 0:
        wordSet.clear()
        for i in range(len(string)):
            hold += string[i]
            wordSet.add(hold)

        longestPali = ""
        for word in wordSet:
            left = word[0:len(word)//2]
            if len(word) % 2 != 0:
                right = word[len(word)//2 + 1:len(word)] 
            else:
                right = word[len(word)//2:len(word)]
            
            if left == right[::-1]:
                if len(word) > len(longestPali):
                    longestPali = word

        answer = answer[len(longestPali)::]

    return answer

answer = codedoc2("abbaeemeet")
print(answer)