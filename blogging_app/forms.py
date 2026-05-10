from django import forms
from . import models


class CreatePostForms(forms.ModelForm):
    class Meta:
        model = models.Post
        fields = ["title", "description", "content", "is_published"]

        widgets = {
            "title": forms.TextInput(
                attrs={"id": "title_input", "placeholder": "Give a title to your post."}
            ),
            "description": forms.Textarea(
                attrs={
                    "id": "description_input",
                    "placeholder": "Tell what this post is about in short.",
                }
            ),
            "content": forms.Textarea(
                attrs={
                    "id": "content_input",
                    "placeholder": "Explain your thoughts in detail.",
                }
            ),
            "is_published": forms.Select(
                attrs={
                    "id": "status_input",
                    "placeholder": "Select status of the post.",
                }
            ),
        }
