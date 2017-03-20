from django.shortcuts import render
from django.views import View

from chat.models import Room


class ChatView(View):

    def get_object(self, slug):
        obj, _ = Room.objects.get_or_create(slug=slug)
        return obj

    def get(self, request, slug, *args, **kwargs):
        room = self.get_object(slug)
        messages = room.message_set.order_by('created_at')

        return render(request, "chat/room.html", {
            'room': room,
            'messages': messages,
        })

