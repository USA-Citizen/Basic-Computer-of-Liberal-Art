def twoSum(nums:list, target:int) -> list:
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """
    nums2 = nums
    for x in nums:
        for y in nums2:
            if x == y:
                continue
            if (x + y) == target:
                return [x, y]
    return [x, y]

a = [x for x in range(1, 101, 3)]
b = int(input('Please input your integer:'))
s = twoSum(a, b)
print(s)