class Solution:
    def isPalindrome(self, s: str) -> bool:
        if s == " ":
            return True

        i = 0
        j = len(s)-1
        flag = False
        s = s.lower()

        for k in s:
            if k.isalnum():
                flag = True
                break
        if not flag:
            return True

        
        while i <= j and i < len(s) and j >= 0:
            while i < len(s) and not s[i].isalnum():
                # print(s[i], 'i')
                i+=1
                
            while j >= 0 and not s[j].isalnum():
                # print(s[j], 'j')
                j-=1
                
            
            if  i < len(s) and j >= 0 and s[i] == s[j]:
                i += 1
                j -= 1
            
            else:
                return False
        return True