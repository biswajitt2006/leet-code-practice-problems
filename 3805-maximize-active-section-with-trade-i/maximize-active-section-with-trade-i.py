from itertools import groupby

class Solution:
    def maxActiveSectionsAfterTrade(self, s: str) -> int:
        t = "1" + s + "1"

        runs = []
        for ch, grp in groupby(t):
            runs.append((ch, len(list(grp))))

        ones = s.count("1")
        best_gain = 0

        # Internal 1-runs only
        for i in range(2, len(runs) - 1, 2):
            if runs[i][0] == '1':
                left_zero = runs[i - 1][1]
                right_zero = runs[i + 1][1]
                best_gain = max(best_gain, left_zero + right_zero)

        return ones + best_gain
        

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna