# Card dump scripts

The scripts written in this folder can get data from all currently available Yu-Gi-Oh! cards in the <a href="https://db.ygoprodeck.com/api-guide/">YGOPRODeck API</a>, as well as filtering the relevant data to feed a PostgreSQL table.

The main script `dump_to_db.py` is responsible for joining the smaller functions in the other files, as well as connecting to the database. Once a list of all cards (which are stored in dicts) is obtained from the code in `card_search.py`. Once the list of cards is obtained, it'll be iterated on and each card there will be filtered according to its type (monster or spell/trap). The functions in `card_filters.py` return a dict with only the relevant info for each card to be inserted into the DB, as well as setting up the CharFields and TextFields to have escaped characters such as quotes. The `db_operations.py` file contains the SQL commands to insert each card into the table, and prints to the console if the insertion was successful or not.

## Current issues:

-   The code in `card.filters.py` can be optimized for less repetition.
