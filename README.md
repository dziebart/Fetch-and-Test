# Fetch-and-Test
Small Python script to fetch data from MongoDB, apply tests to it and write the results to another database, while continuously monitoring and fetching new data inserted into the database.

## Requirements

This is a highly specific script, so it will only work in the context of the database structure defined in the code. To adapt the Code for other databases you would have to adapt methods in master.py, slave.py and stat_result.py.

Therefore, the current requirements are a *MongoDB*, a *MySQL DB* (including the table structures defined in the code) and dieharder. The classes themselves also use *pymongo*  and *sqlalchemy*.

Note, that the Code currently only works on Linux system and was tested and executed on *Debian 10 Buster* and requires *Python 3*.

## Run the Script

Adapt the database URL, database name and database tables in master.py and execute 

`python3 master.py`

## Acknowledgements

This script was created in the course of the Master-thesis "Blackbox Evaluation of TLS Randomness" at Paderborn University.
