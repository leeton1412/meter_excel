from django.conf.urls import url
from .views import index, data

urlpatterns = [
    url(r'^$', index, name='index'),

    url(r'data', data, name='data'),
]
