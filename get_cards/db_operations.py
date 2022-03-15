import psycopg2


def insert_monster_card(card:dict, cursor) -> None:
    if 'def' in card.keys():
        defense = card['def']
    else:  
        defense = 'NULL' # Link monsters do not have defense values
    
    cursor.execute(
        "INSERT INTO public.api_cardmodel "
        "(card_name, card_attribute, card_level, card_type, card_description, card_race, card_atk, card_def) "
        "VALUES "
        f"('{card['name']}', '{card['attribute']}', '{card['level']}', '{card['type']}', '{card['desc']}', '{card['race']}', {card['atk']}, {defense});"
        )

    print(f"Added card {card['name']} to the database successfully!")

def insert_spell_or_trap_card(card: dict, cursor) -> None:
    cursor.execute(
        "INSERT INTO public.api_cardmodel (card_name, card_type, card_description, card_race) "
        "VALUES "
        f"('{card['name']}', '{card['type']}', '{card['desc']}', '{card['race']}')"
    )
    print(f"Added card {card['name']} to the database successfully!")
