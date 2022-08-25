def primeCount(n):

    nums = [i for i in range(2, n + 1)]
    
    iter = nums[0]
    while iter * iter <= n:

        for x in range(iter * 2, n, iter):
        
            nums[x] == 0
        
        iter += 1

        while iter == 0:
            iter += 1
    
    answer = 0

    for num in nums:
        if num == 0:
            answer +=1
print()
primeCount(20)