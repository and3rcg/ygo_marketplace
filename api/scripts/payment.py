from django.contrib.auth import get_user_model

User = get_user_model()


def make_transaction(user, price, deduce=True):
    """
    This is a basic payment algorithm that works as follows:
        user is an user from api.models
        if deduce is set to True, the user's wallet will be deduced by price

    This function should be changed to use an actual payment API, as it is right now a simplified
    abstraction of how the money transfers should work.
    """
    if deduce is True:
        price = price * -1
    user.wallet += price
    user.save()
