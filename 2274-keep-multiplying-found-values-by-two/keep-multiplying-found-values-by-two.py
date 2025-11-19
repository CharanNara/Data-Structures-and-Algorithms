class Solution:
    def findFinalValue(self, nums: List[int], original: int) -> int:
        setnums = set(nums)

        while original in setnums:
            original = original * 2
        return original        