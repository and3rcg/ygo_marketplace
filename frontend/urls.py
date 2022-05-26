from django.urls import include, path
from .views import *

urlpatterns = [
    path('', index),  # card_list
    path('checkout/', index, name='checkout'),
    path('detail/<int:pk>', CardDetailsView.as_view(), name='details'),
    path('login/', index, name='login'),
    path('profile/edit', index, name='edit_profile'),
    path('user/<username>', index, name='user_profile'),
    path('register/', UserRegisterView.as_view(), name='register'),
]
