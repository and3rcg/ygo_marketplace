from django.db.models import F
from django.contrib.auth import get_user_model

User = get_user_model()


def make_transaction(seller, buyer, price, shipping_fee=5):
    """
    This is a basic payment algorithm that works as follows:
        seller and buyer are users from api.models
        the website (in this case, admin) will take a 10% cut of every transaction;
        the seller takes the 90% remaining of the transaction's price
        the buyer's wallet is deduced by the order's price (with the shipping fee)

    This function should be changed to use an actual payment API, as it is right now a simplified
    abstraction of how the money transfers should work.
    """
    admin = User.objects.get(username='admin')

    admin.wallet = F('wallet') + 0.1*price
    admin.save()
    seller.wallet = F('wallet') + 0.9*price
    seller.save()
    buyer.wallet = F('wallet') - (price + shipping_fee)
    buyer.save()
