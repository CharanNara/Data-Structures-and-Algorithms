class Solution:
    def isOneBitCharacter(self, bits: List[int]) -> bool:
        i = 0
        while(i < len(bits)-1):
            if bits[i] == 1:
                if (i+1) == len(bits)-1:
                    return False
                i += 2
            else:
                i += 1

        return True

            
"""
bitwise opns
& | >> << ^


[0,0]

[1,0,0]
 0 1 2

 [1,1,1,0]
  0 1 2 3



10 
11


if it starts with one it's 2 bit char

else one bit char
---------------------


"""