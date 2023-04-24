-- Table: MyNumbers

-- +-------------+------+
-- | Column Name | Type |
-- +-------------+------+
-- | num         | int  |
-- +-------------+------+
-- There is no primary key for this table. It may contain duplicates.
-- Each row of this table contains an integer.

-- A single number is a number that appeared only once in the MyNumbers table.
-- Write an SQL query to report the largest single number. If there is no single number, report null.
-- The query result format is in the following example.

-- Input:

-- +---+
-- |num|
-- +---+
-- | 8 |
-- | 8 |
-- | 3 |
-- | 3 |
-- | 1 |
-- | 4 |
-- | 5 |
-- | 6 | 

-- Output:

-- +---+
-- |num|
-- +---+
-- | 6 |

-- Note:
-- If there is no such number, just output null.

-- Solution

SELECT max(t1.num) as num
FROM
(SELECT num, count(*) as total_count
FROM MyNumbers
GROUP BY num
HAVING count(*) = 1) t1
