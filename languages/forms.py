from django import forms

from languages.models import Language


class CreateLanguageForm(forms.ModelForm):
    class Meta:
        model = Language
        fields = ['name', 'compiled', 'learned_at', 'main_paradigm', 'observations']