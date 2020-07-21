from django import forms

class FormName(forms.Form):
    name = forms.CharField(max_length=200, required=False)
    email = forms.EmailField(required=False)
    text = forms.CharField(widget=forms.Textarea , required=False)
    