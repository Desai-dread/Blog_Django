from django.shortcuts import render, redirect, redirect
from django.views.generic.base import View
from .models import Pin
from .forms import PinForm


class PostView(View):
    # Выводим записи
    def get(self, request):
        posts = Pin.objects.all()
        return render(request, 'blog/index.html', {'post_list': posts})

class SoloPage(View):
    """Отдельная страница"""
    def get(self, request, pk):
        post = Pin.objects.get(id=pk)
        return render(request, 'blog/SoloPage.html', {'post': post})

class AddComments(View):
    """Добавляем комментарии"""
    def post(self, request, pk):
        return redirect('/')


def create(request):
    error = ''
    if request.method == 'POST':
        form =PinForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            error = 'ЗАполни форму нормально'

    form = PinForm()
    context = {
        'form': form,
        'error': error
    }
    return render(request, 'blog/create.html', context)