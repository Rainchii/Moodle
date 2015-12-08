from django.conf.urls import include, url
from .views import nueva

urlpatterns = [
    url(r'^nueva/$', nueva, name="nueva"),
]