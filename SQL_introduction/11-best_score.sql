-- List all records of the table second_table  with a score >= 10 and ordered by score.
SELECT score, name 
FROM second_table
WHERE score >= 10
ORDER BY score DESC;
