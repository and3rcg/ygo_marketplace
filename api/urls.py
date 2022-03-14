from django.urls import path, include
from .views import LoginView

urlpatterns = [
    path('login/', include(LoginView.as_view()), name='login'),
]

