class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        # two pointers approach
        # we keep i still until we see a non-val element there by decrementing j accordingly

        i = 0
        j = len(nums)-1
        k = 0

        while i <= j:
            if nums[i] == val:
                nums[i] = nums[j]
                j -= 1

            else:
                i += 1
                k += 1
            

        print(nums)
        return k



"""
Brute force:

1. to use new array and keep adding the elements to the array and skip the val element
and finally return the len of the array

O(N) time, O(N) space



2. inplace (space efficient)
[0,1,2,2,3,0,4,2], val = 2
 0 1 2 3 4 5 6 7

itr 1
i = 0, k = 0
j = 7

itr 2
i = 1, k = 1
j = 7


itr 3
i = 2, k = 2
j = 7

itr 4
i = 2, k = 2
j = 6

itr 5
i = 2, k = 2
j = 5

[0,1,4,2,3,0,2,2]
 0 1 2 3 4 5 6 7
 k = 3 



######
[3,2,2,3], val = 3
 0 1 2 3

i = 0
j = 3

[3,2,2,3]
 0 1 2

i = 0
j = 2

[2,2,2,3]
 0 1 

i = i + 1

i = 1
j = 1

until i <= j omits the condition


i = 2
j = 1

break the loop

[2,2]


k = 2
return 2


"""