-- Table: Courses

-- +---------+------------+
-- | student | class      |
-- +---------+------------+
-- | A       | Math       |
-- | B       | English    |
-- | C       | Math       |
-- | D       | Biology    |
-- | E       | Math       |
-- | F       | Computer   |
-- | G       | Math       |
-- | H       | Math       |
-- | I       | Math       |
-- +---------+------------+

-- (student, class) is the primary key column for this table.
-- Each row of this table indicates the name of a student and the class in which they are enrolled.

-- Write an SQL query to report all the classes that have at least five students.
-- Return the result table in any order.
-- The query result format is in the following example.

-- Output:
-- +---------+
-- | class   |
-- +---------+
-- | Math    |
-- +---------+

-- Solution

SELECT class FROM
(SELECT class, count(class) AS class_total
FROM Courses
GROUP BY class) count_class_table
WHERE class_total >= 5
