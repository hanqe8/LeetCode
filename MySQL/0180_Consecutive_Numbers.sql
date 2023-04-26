-- Table: Logs

-- +-------------+---------+
-- | Column Name | Type    |
-- +-------------+---------+
-- | id          | int     |
-- | num         | varchar |
-- +-------------+---------+
-- id is the primary key for this table.
-- id is an autoincrement column.
 
-- Write an SQL query to find all numbers that appear at least three times consecutively.
-- Return the result table in any order.
-- The query result format is in the following example.

-- Input: 
-- Logs table:

-- +----+-----+
-- | id | num |
-- +----+-----+
-- | 1  | 1   |
-- | 2  | 1   |
-- | 3  | 1   |
-- | 4  | 2   |
-- | 5  | 1   |
-- | 6  | 2   |
-- | 7  | 2   |
-- +----+-----+

-- Output: 

-- +-----------------+
-- | ConsecutiveNums |
-- +-----------------+
-- | 1               |
-- +-----------------+

-- Explanation: 1 is the only number that appears consecutively for at least three times.

-- Solution

# shift down id by 1 and 2 respectively
# check if num = current num at id 1
# less efficient method and not flexible (where n = x)
SELECT DISTINCT num AS ConsecutiveNums
FROM Logs
WHERE (id + 1, num) IN (SELECT * FROM Logs) AND (id + 2, num) IN (SELECT * FROM Logs)

# alternative method
SELECT DISTINCT num as ConsecutiveNums 
FROM
(SELECT num, SUM(t3) OVER (ORDER BY id) AS flag # include running sum of flag based on value provided by t3 (to group rows with same num)
FROM
(SELECT id, num, CASE WHEN LAG(num) OVER (ORDER BY id) = num # calculate t3 value for each row (if num same as previous row, assign 0 else 1)
THEN 0 ELSE 1 END AS t3
FROM Logs) t1) t2
GROUP BY num, flag
HAVING COUNT(*) >= 3
