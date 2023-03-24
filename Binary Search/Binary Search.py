class Solution:
    def search(self, nums: List[int], target: int) -> int:
        d = dict(enumerate(nums))
        d = dict([(value, key) for key, value in d.items()])
        while True:
            numLen = len(nums)
            index = round(numLen / 2)
            targetVal = d.get(target)
            if numLen <= 1:
                if nums[0] == target:
                    return targetVal
                else:
                    return -1
            if nums[index] == target:
                return targetVal
            if nums[index] < target:
                nums = nums[index:numLen]
            else:
                nums = nums[0:index]