def longestPalindrome(words):
    wordDict = {}
    doubleFlag = False
    counter = 0

    for word in words:
        if word not in wordDict:
            wordDict[word] = 1
        else:
            wordDict[word] = wordDict.get(word) + 1
            
    for word in wordDict:
        if word[::-1] != word:
            if word[::-1] in wordDict and word in wordDict:
                counter += min(wordDict.get(word), wordDict.get(word[::-1]))
                
        if word[::-1] == word:
            if wordDict[word] == 1:
                doubleFlag = True
            if wordDict[word] % 2 == 0:
                counter += wordDict.get(word)
            if wordDict[word] % 2 != 0:
                counter += wordDict.get(word) - 1
                doubleFlag = True
    
    answer = counter * 2
    if doubleFlag:
        answer += 2

    return answer

words = ["lc","cl","gg"]
word = ["lc", "cl"]
doubles = ["aa", "bb", "bb", "aa"]
manyDoubles = ["dd","aa","bb","dd","aa","dd","bb","dd","aa","cc","bb","cc","dd","cc"]
error = ["ll","lb","bb","bx","xx","lx","xx","lx","ll","xb","bx","lb","bb","lb","bl","bb","bx","xl","lb","xx"]
check = ['ee', 'em', 'me', 'em', 'em', 'me', 'me']
checkLong = ["em","pe","mp","ee","pp","me","ep","em","em","me"]
longestPalindrome(manyDoubles)
manyDoubles.sort()
print(manyDoubles)