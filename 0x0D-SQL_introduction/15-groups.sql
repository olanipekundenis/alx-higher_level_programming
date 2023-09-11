--list score from second table in descending order
SELECT score, COUNT(1) AS number FROM second_table GROUP BY score ORDER BY number DESC;
