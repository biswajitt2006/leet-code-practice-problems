/* Write your T-SQL query statement below */
SELECT c.name AS Customers
FROM Customers C 
LEFT JOIN Orders o 
ON c.id=o.customerId
WHERE o.customerId IS NULL

-- Synced seamlessly with LeetHub Pro
-- Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
-- Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna