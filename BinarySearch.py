def binarySearch(numbers, target):
    median = len(numbers)//2
    print(median)
    for i in range(median, 0, -1):
        print(i)
        if numbers[i] == target:
            return i
        if numbers[i + 1] == target:
            return (i + 1)
    
    return -1
nums = [-1,0,3,5,9,12]
answer = binarySearch(nums, 9)
print(answer)