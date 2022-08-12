def longestConsecutive(nums):
    if len(nums) == 0:
        return 0
    setList = set(nums)
    print(setList)
    sortList = sorted(setList)
    listOfSet = []
    print(sortList)
    ans = [sortList[0]]

    for i in range(len(sortList)-1):
        if (sortList[i+1] - sortList[i] == 1):
            if len(ans) ==0:
                ans.append(sortList[i])
            ans.append(sortList[i+1])
        else:
            listOfSet.append(ans.copy())
            ans.clear()

    listOfSet.append(ans.copy())
    listOfSet.sort(key=len, reverse=True)
    print(listOfSet[0])
    return listOfSet[0]


nums = [100,4,200,1,3,2,1]
negative = [9,1,4,7,3,-1,0,5,8,-1,6]

longestConsecutive(negative)