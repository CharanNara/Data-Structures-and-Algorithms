class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        ops = 0
        for i in range(len(nums)):
            if nums[i] % 3 != 0:
                ops += min(nums[i] % 3, -nums[i] % 3)
        return ops
            