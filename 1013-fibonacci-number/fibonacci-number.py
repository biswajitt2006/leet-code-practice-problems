class Solution:
    def fib(self, n: int) -> int:
        dp = {}

        def solve(n):
            if n <= 1:
                return n
            if n in dp:
                return dp[n]
            
            dp[n] = solve(n-1) + solve(n-2)
            return dp[n]
        
        return solve(n)

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna