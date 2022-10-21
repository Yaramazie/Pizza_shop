from django.shortcuts import render, HttpResponse, redirect
from .models import *
from .forms import *
from django.core.mail import send_mail
from django.contrib import messages


def index(request):
    return render(request, 'products/index.html')


def menu(request):
    pizzas = Pizza.objects.filter(available=True)
    slices = PizzaSlice.objects.filter(available=True)
    rolls = PizzaRoll.objects.filter(available=True)
    boxes = Box.objects.filter(available=True)
    topings = Toping.objects.filter(available=True)
    context = {
        'pizzas': pizzas,
        'slices': slices,
        'rolls': rolls,
        'boxes': boxes,
        'topings': topings,

    }
    return render(request, 'products/menu.html', context=context)


def pizzas(request):
    pizzas = Pizza.objects.filter(available=True)
    context = {'pizzas': pizzas}
    return render(request, 'products/pizzas.html', context=context)


def about(request):
    return render(request, 'products/about.html')


def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            mail = send_mail(form.cleaned_data['name'], form.cleaned_data['content'], '4220d8bb32ef69',
                             ['example@gmail.com', 'example2@mail.ru'], fail_silently=False)
            if mail:
                messages.success(request, 'Success')
                return redirect('home')
            else:
                messages.error(request, 'Sending error')
    else:
        form = ContactForm()
    return render(request, 'products/contact.html', {'form': form})
