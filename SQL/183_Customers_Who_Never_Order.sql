-- Table: Customers

-- +----+-------+
-- | Id | Name  |
-- +----+-------+
-- | 1  | Joe   |
-- | 2  | Henry |
-- | 3  | Sam   |
-- | 4  | Max   |
-- +----+-------+

-- id is the primary key column for this table.
-- Each row of this table indicates the ID and name of a customer.

-- Table: Orders

-- +----+------------+
-- | Id | CustomerId |
-- +----+------------+
-- | 1  | 3          |
-- | 2  | 1          |
-- +----+------------+

-- id is the primary key column for this table.
-- customerId is a foreign key of the ID from the Customers table.
-- Each row of this table indicates the ID of an order and the ID of the customer who ordered it.

-- Write an SQL query to report all customers who never order anything.
-- Return the result table in any order.
-- The query result format is in the following example.

-- +-----------+
-- | Customers |
-- +-----------+
-- | Henry     |
-- | Max       |
-- +-----------+

-- Solution
Select name as Customers
from Customers
where id != All(Select c.id from Customers c, Orders o
                where c.id = o.customerId)
