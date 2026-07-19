class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)

        dp = [0, 0, 0]

        for i in range(2, n + 1):
            dp[2] = min(
                dp[1] + cost[i - 1],
                dp[0] + cost[i - 2]
            )
            dp[0] = dp[1]
            dp[1] = dp[2]

        return dp[2]

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna