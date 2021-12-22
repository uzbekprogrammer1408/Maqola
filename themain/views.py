from django.shortcuts import redirect, render
from .models import Articles
from .forms import ArticlesForm

# Create your views here.
def maqola(request):
    maqolalar = Articles.objects.order_by('-sana')
    return render(request, 'themain/maqola.html', {'maqolalar': maqolalar})

def create(request):
    error = ''
    if request.method == "POST":
        form = ArticlesForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('maqolalar')
        else:
            error = "Shakl noto\'g\'ri to\'ldirildi."
            
    form = ArticlesForm

    data = {
        'form': form,
        'error': error
    }
    return render(request, 'themain/create.html', data)

