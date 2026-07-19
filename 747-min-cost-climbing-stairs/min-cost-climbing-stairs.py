class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        dp = [-1] * (n + 1)

        def minCost(n):
            if n <= 1:
                return 0

            if dp[n] != -1:
                return dp[n]

            dp[n] = min(
                minCost(n - 1) + cost[n - 1],
                minCost(n - 2) + cost[n - 2]
            )

            return dp[n]

        return minCost(n)

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna