from django import forms
from .models import Tag, Task


class TaskSearchForm(forms.Form):
    name = forms.CharField(
        max_length=255,
        required=False,
        label="",
        widget=forms.TextInput(
            attrs={"placeholder": "Search by name..."}
        )
    )


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


class TaskForm(forms.ModelForm):

    class Meta:
        model = Task
        fields = ["name", "content", "deadline_datetime", "tags"]
