class Solution:
    def findGCD(self, nums: List[int]) -> int:
        large=max(nums)
        small=min(nums)
        while large %small !=0 :
            large,small=small,large%small
        return small
        

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna