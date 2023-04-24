-- Table: Customer

-- +------+------+-----------+
-- | id   | name | referee_id|
-- +------+------+-----------+
-- |    1 | Will |      NULL |
-- |    2 | Jane |      NULL |
-- |    3 | Alex |         2 |
-- |    4 | Bill |      NULL |
-- |    5 | Zack |         1 |
-- |    6 | Mark |         2 |
-- +------+------+-----------+

-- id is the primary key column for this table.
-- Each row of this table indicates the id of a customer, their name, and the id of the customer who referred them.

-- Write an SQL query to report the names of the customer that are not referred by the customer with id = 2.
-- Return the result table in any order.
-- The query result format is in the following example.

-- Output: 

-- +------+
-- | name |
-- +------+
-- | Will |
-- | Jane |
-- | Bill |
-- | Zack |
-- +------+

-- Solution

SELECT name
FROM Customer
WHERE referee_id != 2 OR referee_id IS NULL
