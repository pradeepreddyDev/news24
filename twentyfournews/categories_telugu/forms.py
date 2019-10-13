from django import forms
from categories_telugu.models import Contacted_telugu


class ContactedteForm(forms.ModelForm):
    class Meta:
        model = Contacted_telugu
        fields = "__all__"
