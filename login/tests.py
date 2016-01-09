from django.core.urlresolvers import resolve
from django.test import TestCase
from django.http import HttpRequest
from django.template.loader import render_to_string
from login.models import Item

from login.views import home_page

class HomePageTest(TestCase):

	def test_root_url_resolves_to_home_page_view(self):
		found = resolve('/')
		self.assertEqual(found.func, home_page)

	def test_home_page_returns_correct_html(self):
		request = HttpRequest()
		response = home_page(request)
		expected_html = render_to_string('home.html')
		self.assertEqual(response.content.decode(), expected_html)

	def test_home_page_can_save_a_POST_request(self):
		request = HttpRequest()
		request.method = 'POST'
		request.POST['location_text'] = 'Location Text'

		response = home_page(request)

		self.assertIn('Location Text', response.content.decode())
		expected_html = render_to_string(
			'home.html',
			{'new_location_text': 'Location Text'}
			)
		self.assertEqual(response.content.decode(), expected_html)

# class ItemModelTest(TestCase):

# 	def test_saving_and_retrieving_items(self):
# 		first_item = Item()
# 		first_item.text = 'The first (ever) list item'
# 		first_item.save()

# 		second_item = Item()
# 		second_item.text = 'Item the second'
# 		second_item.save()

# 		saved_items = Item.objects.all()
# 		self.assertEqual(saved_items.count(), 2)

# 		first_saved_item = saved_items[0]
# 		second_saved_item = saved_items[1]
# 		self.assertEqual(first_saved_item.text, 'The first (ever) list item')
# 		self.assertEqual(second_saved_item.text, 'Item the second')