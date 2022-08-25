def longestCommonPrefix(words):
    #find shortest word
    shortestWord = words[0]
    for word in words:
        if len(word) < len(shortestWord):
            shortestWord = word


    answer = ""

    for i in range(len(shortestWord)):
        letterSet = set()
        for j in range(len(words)):
            letterSet.add(words[j][i])
        if len(letterSet) > 1:

            return answer
        else:
            answer=answer+words[j][i]

    return answer

def sort1(a):

    for i in range(len(a)//2):
        print(i)
        print(a[i], a[len(a)-i])
        if a[i] != a[len(a) - i] - 1:
            return False
            
    return True

def solution(numbers, left, right):
    answer = []
    flag = False
    for i in range(len(numbers)):
        for j in range(left, right):
            if (i+1) * j >= left and (i+1) * j <= right:
                flag = True
            else:
                flag = False
        answer.append(flag)
    print(answer)
    return answer

wordList = ["flower","flow","flight"]
longestCommonPrefix(wordList)

solution([8, 5, 6, 16, 5], 1, 3)
sort1([1, 3, 5, 6, 4, 2])