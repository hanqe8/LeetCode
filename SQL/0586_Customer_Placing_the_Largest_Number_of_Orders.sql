-- Table: Orders

-- | Column            | Type      |
-- |-------------------|-----------|
-- | order_number (PK) | int       |
-- | customer_number   | int       |
-- | order_date        | date      |
-- | required_date     | date      |
-- | shipped_date      | date      |
-- | status            | char(15)  |
-- | comment           | char(200) |

-- Write an SQL query to find the customer_number for the customer who has placed the largest number of orders.
-- The test cases are generated so that exactly one customer will have placed more orders than any other customer.
-- The query result format is in the following example.

-- Sample Input

-- | order_number | customer_number | order_date | required_date | shipped_date | status | comment |
-- |--------------|-----------------|------------|---------------|--------------|--------|---------|
-- | 1            | 1               | 2017-04-09 | 2017-04-13    | 2017-04-12   | Closed |         |
-- | 2            | 2               | 2017-04-15 | 2017-04-20    | 2017-04-18   | Closed |         |
-- | 3            | 3               | 2017-04-16 | 2017-04-25    | 2017-04-20   | Closed |         |
-- | 4            | 3               | 2017-04-18 | 2017-04-28    | 2017-04-25   | Closed |         |


-- Sample Output

-- | customer_number |
-- |-----------------|
-- | 3               |

-- Explanation

-- The customer with number 3 has two orders, which is greater than either customer 1 or 2 because each of them only has one order. 
-- So the result is customer_number 3.


-- Solution

SELECT customer_number FROM
(SELECT customer_number, count(customer_number) AS order_total
FROM Orders
GROUP BY customer_number
ORDER BY order_total DESC LIMIT 1) AS max_order_total
