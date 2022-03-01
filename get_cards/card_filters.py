def monster_filter(card:dict) -> dict:
    # This function will return a dict with only the relevant data

    card_output = {}

    card_output['name'] = card['name']
    card_output['desc'] = card['desc']

    if "'" in card_output['name']:
        # Escaping single quotes when inserting into Postgres
        card_output['name'] = card_output['name'].replace("'", "''")

    if "'" in card_output['desc']:
        # Escaping single quotes when inserting into Postgres
        card_output['desc'] = card_output['desc'].replace("'", "''")

    card_output['race'] = card['race']
    card_output['attribute'] = card['attribute']
    card_output['type'] = card['type']
    card_output['atk'] = int(card['atk'])

    if "Link" in card['type']:
        # Link monsters do not have DEF values
        card_output['level'] = int(card['linkval'])

    else:
        # Any other kind of monster card
        card_output['level'] = int(card['level'])
        card_output['def'] = int(card['def'])

    return card_output


def spell_trap_filter(card:dict) -> dict:
    # This function will return a dict with only the relevant data

    card_output = {}

    card_output['name'] = card['name']
    if "'" in card_output['name']:
        card_output['name'] = card_output['name'].replace("'", "''")

    card_output['race'] = card['race']
    card_output['type'] = card['type']

    card_output['desc'] = card['desc']
    if "'" in card_output['desc']:
        card_output['desc'] = card_output['desc'].replace("'", "''")
    
    return card_output
