from django.urls import path
from .views import RedirectView

urlpatterns = [
    path('<str:key>/', RedirectView.as_view(), name='redirect'),
]