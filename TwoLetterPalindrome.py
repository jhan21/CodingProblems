class TwoLetterPalindrome:

    def longestPalindrome(words):
        singleDoubleFlag = False
        count = 0
        skipSet = set()
        for word in words:
            if word[::-1] in words and word[::-1] != word and word not in skipSet:
                count += min(words.count(word), words.count(word[::-1]))
                skipSet.add(word)

            if word[::-1] == word:
                if words.count(word) == 1 or words.count(word) % 2 != 0:
                    singleDoubleFlag = True
                if words.count(word) % 2 == 0:
                    count += 1
                elif word not in skipSet:
                    count += words.count(word) - 1
                    skipSet.add(word)

            reverseCount = count * 2
            if singleDoubleFlag:
                reverseCount += 2

        return reverseCount
    
    words = ["lc","cl","gg"]
    word = ["lc", "cl"]
    doubles = ["aa", "bb", "bb", "aa"]
    manyDoubles = ["dd","aa","bb","dd","aa","dd","bb","dd","aa","cc","bb","cc","dd","cc"]
    error = ["ll","lb","bb","bx","xx","lx","xx","lx","ll","xb","bx","lb","bb","lb","bl","bb","bx","xl","lb","xx"]
    check = ['ee', 'em', 'em', 'em', 'me', 'me']
    checkLong = ["em","pe","mp","ee","pp","me","ep","em","em","me"]
    answer = longestPalindrome(checkLong)
    print(answer)



