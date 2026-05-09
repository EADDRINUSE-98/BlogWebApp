from django import forms
from . import models


class CreatePostForms(forms.ModelForm):
    class Meta:
        model = models.Post
        fields = ["title", "description", "content", "is_published"]

        widgets = {
            "title": forms.TextInput(attrs={"id": "title_input"}),
            "description": forms.Textarea(attrs={"id": "description_input"}),
            "content": forms.Textarea(attrs={"id": "content_input"}),
        }
