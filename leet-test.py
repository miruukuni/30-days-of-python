def missingMultiple(self, nums, k: int) -> int:
    for i in range(1, 100):
        i = 0
        multiples = k * (i+1)
        if multiples not in nums:
            return multiples
    return multiples

nums = [8, 2, 3, 4, 6]
missingMultiple(1, nums, 2)



#                       ----------------------------------------------------

nums = [2, 7, 11, 15]
target = 9

for i in range(len(nums)):
    for j in range(i + 1, len(nums)):
        if nums[i] + nums[j] == target:
            print(nums[i], nums[j])
            break
    else:
        continue
    break