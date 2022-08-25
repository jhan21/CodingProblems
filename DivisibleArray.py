def findDivisible(arr, k):
    dict = {}
    for num in arr:
        if num % k not in dict:
            dict[num % k] = 1
        else:
            dict[num % k] += 1

    print(dict)

arr = [1,2,3,4,5]

findDivisible(arr, 3)