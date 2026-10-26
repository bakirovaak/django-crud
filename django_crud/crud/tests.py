from django.test import TestCase
from django.urls import reverse

from .models import Item


class ItemCrudTests(TestCase):
    def setUp(self):
        self.item = Item.objects.create(title='Тест', price=10)

    def test_list(self):
        r = self.client.get(reverse('crud:list'))
        self.assertContains(r, 'Тест')

    def test_search(self):
        Item.objects.create(title='Другое')
        r = self.client.get(reverse('crud:list'), {'q': 'Дру'})
        self.assertContains(r, 'Другое')
        self.assertNotContains(r, 'Тест')

    def test_detail(self):
        r = self.client.get(self.item.get_absolute_url())
        self.assertEqual(r.status_code, 200)

    def test_create(self):
        r = self.client.post(reverse('crud:create'), {'title': 'Новая', 'price': '5.50', 'is_active': 'on'})
        self.assertRedirects(r, reverse('crud:list'))
        self.assertTrue(Item.objects.filter(title='Новая').exists())

    def test_update(self):
        r = self.client.post(reverse('crud:update', args=[self.item.pk]), {'title': 'Изм', 'price': '1'})
        self.assertRedirects(r, reverse('crud:list'))
        self.item.refresh_from_db()
        self.assertEqual(self.item.title, 'Изм')

    def test_delete(self):
        r = self.client.post(reverse('crud:delete', args=[self.item.pk]))
        self.assertRedirects(r, reverse('crud:list'))
        self.assertFalse(Item.objects.exists())
