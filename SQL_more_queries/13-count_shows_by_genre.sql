-- Lists all genres from hbtn_0d_tvshows and displays the number of shows linked to each.
SELECT genre genre COUNT(*) number_of_shows
FROM hbtn_0d_tvshows
GROUP BY genre
HAVING COUNT(*) > 0
ORDER BY COUNT(*) DESC;
