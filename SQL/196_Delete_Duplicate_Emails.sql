-- Table: Person

-- +----+------------------+
-- | Id | Email            |
-- +----+------------------+
-- | 1  | john@example.com |
-- | 2  | bob@example.com  |
-- | 3  | john@example.com |
-- +----+------------------+

-- id is the primary key column for this table.
-- Each row of this table contains an email. The emails will not contain uppercase letters.

-- +----+------------------+
-- | Id | Email            |
-- +----+------------------+
-- | 1  | john@example.com |
-- | 2  | bob@example.com  |
-- +----+------------------+

-- Write an SQL query to delete all the duplicate emails, keeping only one unique email with the smallest id. Note that you are supposed to write a DELETE statement and not a SELECT one.
-- After running your script, the answer shown is the Person table. The driver will first compile and run your piece of code and then show the Person table. The final order of the Person table does not matter.
-- The query result format is in the following example.

-- Solution

With table1 as
(Select *,
row_number() over(partition by email order by id) as rk
from person)
Delete from person
where id in (Select table1.id from table1 where table1.rk>1)
