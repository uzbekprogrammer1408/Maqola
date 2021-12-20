from django.shortcuts import render
from .models import Articles
from .forms import ArticlesForm

# Create your views here.
def maqola(request):
    maqolalar = Articles.objects.order_by('-sana')
    return render(request, 'themain/maqola.html', {'maqolalar': maqolalar})

def create(request):
    form = ArticlesForm

    data = {
        'form': form
    }

    return render(request, 'themain/create.html', data)