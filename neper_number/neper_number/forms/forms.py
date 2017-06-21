from django import forms


class CalculateNeperNumberForm(forms.Form):
    members = forms.IntegerField(required=True)
    threads = forms.IntegerField(initial=1)
    output = forms.CharField(initial='result.txt')
    quiet = forms.BooleanField(initial=False, required=False)
