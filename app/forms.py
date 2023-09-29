# forms.py

from django import forms


class VotacaoAulaForm(forms.Form):
    nota = forms.IntegerField(label="Nota", min_value=0, max_value=10)
