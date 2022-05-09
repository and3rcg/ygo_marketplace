import string
import random


def generate_transaction_id(length):
    id = ''.join(random.choices(string.ascii_uppercase + string.digits, k = length))    
    return str(id)
