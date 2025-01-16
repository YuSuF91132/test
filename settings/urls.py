from django.urls import path
from settings.views import index, news, contact

urlpatterns = [
    path("", index),
    path("news/", news),
    path("contact/", contact)
]