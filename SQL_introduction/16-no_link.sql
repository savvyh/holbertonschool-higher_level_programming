-- List all record of second_table, display the score and the name.
SELECT score, name
FROM second_table
WHERE name != ''
ORDER BY score DESC;