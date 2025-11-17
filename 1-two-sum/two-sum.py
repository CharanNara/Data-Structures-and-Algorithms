class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hmap = {}

        for i in range(len(nums)):
            if target - nums[i] in hmap:
                return [i, hmap[target-nums[i]]]
            
            hmap[nums[i]] = i
        
