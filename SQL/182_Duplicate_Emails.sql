-- Table: Person

-- +----+---------+
-- | Id | Email   |
-- +----+---------+
-- | 1  | a@b.com |
-- | 2  | c@d.com |
-- | 3  | a@b.com |
-- +----+---------+

-- Write an SQL query to report all the duplicate emails. Note that it's guaranteed that the email field is not NULL.
-- Return the result table in any order.
-- The query result format is in the following example.

-- +---------+
-- | Email   |
-- +---------+
-- | a@b.com |
-- +---------+

-- Solution
Select Email
from
(Select Email, count(Email)
from Person
group by Email having count(Email)>1) a
