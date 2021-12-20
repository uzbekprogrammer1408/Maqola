from .models import Articles
from django.forms import ModelForm, fields


class ArticlesForm(ModelForm):
    class Meta:
        model = Articles
        fields = ['title', 'matn', 'muallif', 'sana']