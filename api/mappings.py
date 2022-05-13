filters_mapping = {
    # keys = keys from the incoming request's data
    # values = kwargs for the queryset.filter method
    # will add more params in the future (card type, attribute, monster race, etc.)
    'card_name': 'card__name__icontains',
    'username': 'seller__username',
    'card_id': 'card__id',
    'type': 'card__type__icontains',
}
