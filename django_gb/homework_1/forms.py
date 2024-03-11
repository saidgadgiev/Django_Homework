from django import forms


class GetProductClientDays(forms.Form):
    id_client = forms.IntegerField()
    days = forms.IntegerField()
