from django.urls import path
from .views import home, submissions

urlpatterns = [
    path('', home, name='home'),
    path('submissions/', submissions, name='submissions'),
]
