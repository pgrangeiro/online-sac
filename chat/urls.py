from django.conf.urls import url
from chat.views import ChatView


app_name = 'chat'

urlpatterns = [
    url(r'^(?P<slug>\w+)/', ChatView.as_view(), name='room'),
]
