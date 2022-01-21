from django import forms

from home.models import posty


class postyForm(forms.ModelForm):
    class Meta:
        model = posty
        fields = '__all__'
        exclude = ('author','like')

