from django import forms


class SearchForm(forms.Form):
    article = forms.IntegerField()


class UpdateExcel(forms.Form):
    excel_file = forms.FileField()
