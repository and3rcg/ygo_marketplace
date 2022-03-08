from api.models import CardModel
from django.shortcuts import render
from django.views.generic import ListView, DetailView


# TODO: The "index" view should be a list of all cards, from the CardsOnSale method (no duplicates)
def index(request, *args, **kwargs):
    return render(request, 'frontend/index.html')


class CardDetailsView(DetailView):
    template_name = 'frontend/detail.html'
    model = CardModel

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['card'] = self.get_object()
        print(context['card'])
        # insert cards on sale: CardsOnSale.objects.filter(card_id)
        return context


# TODO: View for card search (ListView)
