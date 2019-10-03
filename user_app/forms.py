from django import forms
from .models import User


class NewUserForm(forms.ModelForm):
    class Meta():
        model = User
        fields = '__all__'


class ContactForm(forms.ModelForm):
    class Meta():
        model = User
        fields = '__all__'

    def clean_email(self):
        data = self.cleaned_data['email']
        if "fred" not in data:
            msg = "You have forgotten about Fred!"
            self.add_error('first_name', msg)
            raise forms.ValidationError(msg)

        # Always return a value to use as the new cleaned data, even if
        # this method didn't change it.
        return data
