from django.conf.urls import url
from django_tenant.views import HomeView


urlpatterns = [
    url(r'^$', HomeView.as_view()),
]
