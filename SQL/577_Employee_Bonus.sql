-- Table:Employee

-- +-------+--------+-----------+--------+
-- | empId |  name  | supervisor| salary |
-- +-------+--------+-----------+--------+
-- |   1   | John   |  3        | 1000   |
-- |   2   | Dan    |  3        | 2000   |
-- |   3   | Brad   |  null     | 4000   |
-- |   4   | Thomas |  3        | 4000   |
-- +-------+--------+-----------+--------+

-- empId is the primary key column for this table.
-- Each row of this table indicates the name and the ID of an employee in addition to their salary and the id of their manager.

-- Table: Bonus

-- +-------+-------+
-- | empId | bonus |
-- +-------+-------+
-- | 2     | 500   |
-- | 4     | 2000  |
-- +-------+-------+

-- empId is the primary key column for this table.
-- empId is a foreign key to empId from the Employee table.
-- Each row of this table contains the id of an employee and their respective bonus.

-- Example ouput:

-- +-------+-------+
-- | name  | bonus |
-- +-------+-------+
-- | John  | null  |
-- | Dan   | 500   |
-- | Brad  | null  |
-- +-------+-------+

-- Solution

Select e.name, b.bonus
from Employee e left join Bonus b
on e.empId = b.empId
where b.bonus < 1000 or b.bonus IS NULL
