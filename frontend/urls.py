from django.urls import include, path
from .views import *

urlpatterns = [
    path('', index), # card_list
    path('detail/<int:pk>', CardDetailsView.as_view(), name='details'),
    path('register/', UserRegisterView.as_view(), name='register'),
    path('login/', index, name='login'),
    path('logout/', index, name='logout'),
]
