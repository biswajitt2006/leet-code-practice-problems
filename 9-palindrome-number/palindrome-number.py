class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x <0 :
            return False
        
        rev=0
        dup = x 

        while dup > 0 :
            rev=(rev*10)+(dup%10)
            dup //=10
        return rev==x 
        