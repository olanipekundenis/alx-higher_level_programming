--display names by score in descending order
SELECT score, name FROM second_table HAVING name IS NOT NULL ORDER BY score DESC;
