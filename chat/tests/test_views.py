from model_mommy import mommy

from django.core.urlresolvers import reverse_lazy
from django.test import TestCase

from chat.models import Message, Room


class ChatViewTestCase(TestCase):

    def setUp(self):
        self.url = reverse_lazy('chat:room', kwargs={'slug': 'xpto'})

    def test_get_returns_200(self):
        response = self.client.get(self.url)

        self.assertEqual(200, response.status_code)
        self.assertTemplateUsed(response, 'chat/room.html')
        self.assertIn('room', response.context)
        self.assertIn('messages', response.context)

    def test_get_creates_room_if_it_does_not_exist(self):
        self.assertEqual(0, Room.objects.count())

        response = self.client.get(self.url)
        room = Room.objects.get()
        self.assertEqual(room, response.context['room'])

    def test_get_returns_room_if_it_already_exists(self):
        room = mommy.make(Room, slug='xpto')
        room.message_set.add(mommy.make(Message))
        room.message_set.add(mommy.make(Message))
        room.save()

        response = self.client.get(self.url)

        self.assertEqual(room, response.context['room'])
        self.assertEqual(2, len(response.context['messages']))
        for message in room.message_set.all():
            self.assertIn(message, response.context['messages'])
