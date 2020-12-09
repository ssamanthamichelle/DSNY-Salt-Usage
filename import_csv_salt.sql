--Samantha Michelle Garcia
--Import CSV


\copy salt(stormnumber, date, manhattan, bronx, brooklyn, queens, statenisland, totaltons)
FROM '/Users/samanthagarcia/Desktop/DSNY_Salt_CLEAN.csv'
DELIMITER ',' CSV HEADER;
