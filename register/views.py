from django.shortcuts import render
from .forms import RegisterForm

# Create your views here.

def register_view(request):
    form = RegisterForm()
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        print('---555555555555555555555555555555555555')
        if form.is_valid():
            form.save()
    context = { 'form':form }
    return render(request, template_name='themain/register.html', context=context)