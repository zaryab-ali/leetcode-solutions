class Solution:
    def isPalindrome(self, x: int) -> bool:
        s = str(x)
        n = int(len(s)/2)
       
        

        for i in range(n):
            if s[i] != s[-(i+1)]:
                return False
            
        
        return True