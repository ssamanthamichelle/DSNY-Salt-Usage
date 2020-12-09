# DSNY-Salt-Usage

Data Source:  https://catalog.data.gov/dataset/dsny-salt-use-by-day-2015-2017

This dataset aims to record the amount of salt used by each borough on a given day of a storm from 2016 through 2019. It is difficult to measure such a large amount accurately, so the New York City Department of Sanitation (DSNY) records the number of times a piece of salt-spreading equipment reloads and multiplies that by the capacity of a piece of salt-spreading equipment which is 16 tons.


* DSNY_Salt_Usage.csv         -- original dataset
* DSNY_salt.py                -- Python program using Numpy to calculate summary statistics and Matplotlib to create visualizations
* DSNY_salt2.py               -- Python program to clean DSNY_Salt_Usage.csv and create DSNY_Salt_CLEAN.csv
* DSNY_Salt_CLEAN.csv         -- cleaned dataset
* create_table_salt.sql       -- SQL script to create table for DSNY_Salt_CLEAN.csv
* import_csv_salt.sql         -- SQL script to import DSNY_Salt_CLEAN.csv
* salt_queries.sql            -- SQL script to query the data in the PostgreSQL table called 'salt'
* queries_and_results_salt.md -- report which contains the queries from salt_table.sql and their results from running on PostgreSQL
