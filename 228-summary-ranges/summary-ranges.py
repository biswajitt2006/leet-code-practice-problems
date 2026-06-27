from typing import List

class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        res = []
        n = len(nums)
        
        i = 0
        while i < n:
            start = nums[i]
            
            # move while consecutive
            while i + 1 < n and nums[i] + 1 == nums[i + 1]:
                i += 1
            
            end = nums[i]
            
            if start == end:
                res.append(str(start))
            else:
                res.append(f"{start}->{end}")
            
            i += 1
        
        return res
        

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna