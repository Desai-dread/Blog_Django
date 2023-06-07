from .models import Pin, Comments
from django.forms import ModelForm, TextInput, Textarea


class PinForm(ModelForm):
    class Meta:
        model = Pin
        fields = ["tittle", "subTitle", "author", "date"]
        widgets = {
            "tittle": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Название статьи'
            }),
            "subTitle": Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Сама статья'
            }),
            "author": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'автор'
            }),
            "date": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Дата',
                'type': 'date'
            }),
                   }

class CommentsForm(ModelForm):
    class Meta:
        model = Comments
        fields = ["email", "name", "text_comment"]
