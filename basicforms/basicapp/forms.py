from django import forms
from django.core import validators

class FormName(forms.Form):
    name = forms.CharField(max_length=200, required=False)
    email = forms.EmailField(required=False)
    verify_email = forms.EmailField(label='Enter your email again:', required=False)
    text = forms.CharField(widget=forms.Textarea , required=False)

    def clean(self):
        all_clean_data = super().clean()
        email = all_clean_data['email']
        vemail = all_clean_data['verify_email']

        if email != vemail:
            raise forms.ValidationError("MAKE SURE EMAILS MATCH!")