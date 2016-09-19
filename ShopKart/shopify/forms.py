from django.contrib.auth.models import User
from .models import UserProfile
from django import forms


PRODUCT_QUANTITY_CHOICES = [(i, str(i)) for i in range(1, 21)]


class CartAddProductForm(forms.Form):
    quantity = forms.TypedChoiceField(choices=PRODUCT_QUANTITY_CHOICES,
                                      coerce=int)
    update = forms.BooleanField(required=False,
                                initial=False,
                                widget=forms.HiddenInput)


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    class Meta:
        model = User
        fields = ('username', 'email', 'password')

class UserProfileForm(forms.ModelForm):
    remember_me = forms.BooleanField(required=False, widget=forms.CheckboxInput())
    class Meta:
        model = UserProfile
        fields = ('created_date',)



            # def clean(self):
        #     cleaned_data = super(UserProfileForm, self).clean()
        #     print self.cleaned_data.get('remember_me')
        #     if not self.cleaned_data.get('remember_me'):
        #         self.request.session.set_expiry(0)
        #
        #


