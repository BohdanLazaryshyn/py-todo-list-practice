from django import forms
from django.forms import DateInput, TimeInput

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
        fields = ["name", "deadline_date", "deadline_time", "tags"]
        widgets = {
            "deadline_date": DateInput(attrs={"type": "date"}),
            "deadline_time": TimeInput(attrs={"type": "time"}),
            "tags": forms.CheckboxSelectMultiple()
        }

    # class Meta:
    #     model = Task
        # fields = ["name", "deadline_datetime", "tags"]
        # widgets = {"deadline_datetime": forms.widgets.SelectDateWidget(), "tags": forms.CheckboxSelectMultiple()}
