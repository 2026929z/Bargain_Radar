from django.test import TestCase
from radar.models import Category


class CategoryModelTests(TestCase):

    def test_slug_creation(self):
        cat = Category(name='a b c')
        cat.save()
        self.assertEqual(cat.slug, 'a-b-c')


class OfferModelTest(TestCase):

    cat = Category('a')

    def test_neg_price(self):
        offer = Offer(category=cat, representative=None,
                      name='b', price=-1.0)
        offer.save()
        self.assertEqual((offer.price >= 0.0), True)

    def test_neg_amount(self):
        offer = Offer(category=cat, representative=None,
                      name='b', amount=-1)
        offer.save()
        self.assertEqual((offer.amount >= 0), True)

    def test_neg_views(self):
        offer = Offer(category=cat, representative=None,
                      name='b', views=-1)
        offer.save()
        self.assertEqual((offer.views >= 0), True)

    def test_neg_likes(self):
        offer = Offer(category=cat, representative=None,
                      name='b', likes=-1)
        offer.save()
        self.assertEqual((offer.likes >= 0), True)


class LoginViewTest(TestCase):

    def test_page_rendered(selfself):
        response = self.client.get(reverse('login'))
        self.assertEqual(response.status_code, 200)



class RegisterViewTest(TestCase):

    def test_register_page_rendered(selfself):
        response = self.client.get(reverse('register'))
        self.assertEqual(response.status_code, 200)


class LoginViewTest(TestCase):

    def test_login_page_rendered(selfself):
        response = self.client.get(reverse('login'))
        self.assertEqual(response.status_code, 200)


class ContactViewTest(TestCase):

    def test_page_rendered(selfself):
        response = self.client.get(reverse('contact'))
        self.assertEqual(response.status_code, 200)
        self.assertQuerysetEqual(response.context['customer'], [])