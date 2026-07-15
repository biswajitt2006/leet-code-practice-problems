/* Write your T-SQL query statement below */
SELECT DISTINCT num AS ConsecutiveNums
FROM (
    SELECT
        num,
        LAG(num,1) OVER(ORDER BY id) AS prev1,
        LAG(num,2) OVER(ORDER BY id) AS prev2
    FROM Logs
) t
WHERE num = prev1
  AND num = prev2;

-- Synced seamlessly with LeetHub Pro
-- Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
-- Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna