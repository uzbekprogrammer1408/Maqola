from .models import Articles
from django.forms import ModelForm, fields, TextInput, DateTimeInput, Textarea, DateTimeField


class ArticlesForm(ModelForm):
    class Meta:
        model = Articles
        fields = ['title', 'matn', 'muallif', 'sana']

        widgets = {
            'muallif': TextInput(attrs={
                'placeholder': 'Muallif'
            }),
            'title': TextInput(attrs={
                'placeholder': 'Mavzu'
            }),
            'matn': Textarea(attrs={
                'placeholder': 'Matn'
            }),
            'sana': DateTimeInput(attrs={
                'placeholder': 'Sana'
            })
        }