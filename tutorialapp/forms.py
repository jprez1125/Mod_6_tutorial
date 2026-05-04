
from django import forms
from .models import Comment

class NameForm(forms.Form):
    name = forms.CharField(label="Your name", max_length=100)

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ["name", "comment"]
