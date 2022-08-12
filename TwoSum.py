def twoSum(nums, target):

    hashmap = {}
    for i in range(len(nums)):
        remaining = target - nums[i]
        if remaining in hashmap:
            return (i, hashmap[remaining])
        hashmap[nums[i]] = i
    return []

nums = [2,7,11,15]
target = 9

print(twoSum(nums, target))