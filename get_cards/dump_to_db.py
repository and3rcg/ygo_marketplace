from card_search import search_all
from card_filters import monster_filter, spell_trap_filter
from db_operations import insert_monster_card, insert_spell_or_trap_card
import psycopg2


db_connection = psycopg2.connect(
    host='localhost',
    database='postgres',
    user='postgres',
    password='postgres',
    port=5432)

db_cursor = db_connection.cursor()

card_list = search_all() # returns a card list

for card in card_list:
    if "Monster" in card['type']: # collect monster data (is link?)
        dump_card = monster_filter(card)
        insert_monster_card(dump_card, db_cursor)
    
    elif "Spell" or "Trap" in card['type']: # collect spell/trap data
        dump_card = spell_trap_filter(card)
        insert_spell_or_trap_card(dump_card, db_cursor)

    elif "Skill" in card['type']: 
        # these cards are not used in the TCG's traditional format.
        continue


# commit connection before closing!
db_connection.commit()

db_cursor.close()
db_connection.close()