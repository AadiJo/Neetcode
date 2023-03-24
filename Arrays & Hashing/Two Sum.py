class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        ctr = 0
        for i in nums:            
            try:
                index = nums[:ctr].index(target - i)               #### Finding index every iteration of loop
                return [index, ctr]
            except:
                pass
            ctr += 1