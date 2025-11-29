class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        if sum(nums) % k == 0:
            return 0

        x = sum(nums) % k

        if sum(nums) >= x:
            return x
        

"""
min ops to make aray sum divisible by k


[3,9,7] = 16+3 = 19 -- 

if sum(arr) % k == 0 -> return 0


if sum(arr) % k == x -> then we do need to have elements which are greater than x

or actually if sum of all elements is > x then we could actually do those many ops



"""