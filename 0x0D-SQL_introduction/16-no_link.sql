-- A script that lists all records of the table second_table
-- Results should display the score and the name
-- Records shoudl be listed by descending score
SELECT score, name FROM second_table WHERE IS NOT NULL ORDER BY score DESC;
