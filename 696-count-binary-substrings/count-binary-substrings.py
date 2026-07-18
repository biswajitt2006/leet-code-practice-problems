class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        prev=0
        curr=1
        ans=0
        for i in range(1,len(s)):
            if s[i]==s[i-1]:
                curr+=1
            else :
                ans +=min(curr,prev)
                prev=curr
                curr=1
        ans+=min(curr,prev)
        return ans 

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna