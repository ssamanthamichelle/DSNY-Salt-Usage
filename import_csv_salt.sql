--Samantha Michelle Garcia
--Import CSV


\copy salt(stormnumber, date, manhattan, bronx, brooklyn, queens, statenisland, totaltons)
FROM '/Users/samanthagarcia/Desktop/name_your_file.csv'
DELIMITER ',' CSV HEADER;