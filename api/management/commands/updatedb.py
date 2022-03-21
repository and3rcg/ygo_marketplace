from api.models import CardModel
from django.core.management.base import BaseCommand

import requests

# sort cards by latest: first existing card will mean the database is updated.
api_url = 'https://db.ygoprodeck.com/api/v7/cardinfo.php?sort=new'

class Command(BaseCommand):
    help = 'Updates the cards database from the YGOPRODeck API.'
    queryset = CardModel.objects.all()

    def handle(self,*args, **options):
        api_response = requests.get(api_url).json()
        card_list = api_response['data']
        for card in card_list:

            if CardModel.objects.filter(name=card['name']).exists():
                print('Finished updating the cards database!')
                break

            if "Spell" in card['type'] or "Trap" in card['type']:
                db_card = CardModel(name=card['name'], race=card['race'], type=card['type'], description=card['desc'])
            
            elif "Monster" in card['type']:

                if "Link" in card['type']: # is link monster?
                    db_card = CardModel(
                        name=card['name'],
                        attack=card['atk'],
                        level=card['linkval'],
                        attribute=card['attribute'],
                        race=card['race'],
                        type=card['type'],
                        description=card['desc']
                        )
                
                else: # is any other kind of monster?
                    db_card = CardModel(
                        name=card['name'],
                        attack=card['atk'],
                        defense=card['def'],
                        level=card['level'],
                        attribute=card['attribute'],
                        race=card['race'],
                        type=card['type'],
                        description=card['desc']
                        )

            else: # skill cards do not exist in the traditional TCG format.
                continue

            print(f"Added card {card['name']} successfully!")
            db_card.save()