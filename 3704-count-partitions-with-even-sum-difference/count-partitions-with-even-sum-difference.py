class Solution:
    def countPartitions(self, nums: List[int]) -> int:
        index_partition = 0
        first_partition = nums[index_partition]
        second_partition = sum(nums)-nums[index_partition]
        count_even = 1 if abs(second_partition - first_partition) & 1==0 else 0

        for index_partition in range(1,len(nums)-1):
            to_split = nums[index_partition]
            first_partition += to_split
            second_partition -= to_split

            count_even += 1 if abs(second_partition - first_partition) & 1 ==0 else 0
        return count_even



"""
how many partitions are even?

[10,10,3,7,6]
so we first partition at 0, then 1, then 2, then 3

so we could bascially calculate sum(all) then keep removing them and adding it to another partition total 
next find the difference

"""