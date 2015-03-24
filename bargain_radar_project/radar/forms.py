from django import forms
from django.contrib.auth.models import User
from radar.models import Offer, CustomerProfile

# class OfferForm(forms.ModelForm):
#     name = forms.CharField(max_length=128, help_text="Please enter the title of the offer")
#     top = forms.BooleanField(default=False)
#     price = forms.DecimalField(max_digits=7, decimal_places=2, help_text="Please enter the price of the offer" )
#     views = forms.IntegerField(widget=forms.HiddenInput(), initial=0)
#     likes = forms.IntegerField(widget=forms.HiddenInput(), initial=0)
#     description = forms.TextField(max_length=1000, help_text="Please enter the title of the offer")
#     picture = forms.ImageField(upload_to='offer_images')
#
#
#     class Meta:
#         model = Offer
#         exclude = ('category',)
#
#
#     def clean(self):
#         cleaned_data = self.cleaned_data
#         url = cleaned_data.get('url')
#
#         # If url is not empty and doesn't start with 'http://', prepend 'http://'.
#         if url and not url.startswith('http://'):
#             url = 'http://' + url
#             cleaned_data['url'] = url
#
#         return cleaned_data

class CustomerForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'username', 'password')

class CustomerProfileForm(forms.ModelForm):
    class Meta:
        model = CustomerProfile
        fields = ('representative',)