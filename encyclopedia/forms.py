from django import forms

class searchForm(forms.Form):
    searchQuery = forms.CharField(label='q', max_length= 50)
