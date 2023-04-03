from django import forms
from .models import Tag


class TagSearchForm(forms.Form):
    name = forms.CharField(
        max_length=255,
        required=False,
        label="",
        widget=forms.TextInput(
            attrs={"placeholder": "Search by name..."}
        )
    )


class TagForm(forms.ModelForm):

    class Meta:
        model = Tag
        fields = ["name"]
