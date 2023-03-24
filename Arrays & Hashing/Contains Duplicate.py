class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        setList = set(nums)

        if (len(setList) != len(nums)):

            return True

        else:
            
            return False