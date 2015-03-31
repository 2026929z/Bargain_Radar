from django.test import TestCase
from radar.models import Category, Offer, User, CustomerProfile, Basket


class ModelsMethodTests(TestCase):

    def test_ensure_basket_total_positive(self):
        random_user = User.objects.create_user('abc', 'abc@abc.com', 'abc')
        customer = CustomerProfile(user=random_user, representative = True)
        category = Category(name='footwear')
        offer = Offer(category=category, representative=customer, name='shoes', price=10.0)
        basket = Basket(customer=customer, total=-1)
        basket.save()
        self.assertEqual((basket.total >= 0), True)

    def test_ensure_basket_total_positive(self):
        basket.save()
        self.assertEqual((basket.total >= 0), True)
