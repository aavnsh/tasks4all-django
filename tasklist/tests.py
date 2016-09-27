from django.test import TestCase

from tasklist.forms import AddItemForm
from tasklist.models import Item


class ItemMethodTests(TestCase):

    def test_new_item_is_incomplete(self):
        new_item = Item()
        self.assertIs(new_item.completed, False)

    def test_new_item_is_not_overdue(self):
        new_item = Item()
        self.assertIs(new_item.overdue_status(), False)

    def test_add_form_blank_is_invalid(self):
        form_data = {}
        form = AddItemForm(data=form_data)
        self.assertFalse(form.is_valid())

