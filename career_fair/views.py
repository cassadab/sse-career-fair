from django.shortcuts import render


def index(request):
    context = {'home_active': 'active'}
    return render(request, 'index.html', context)


def companies(request):
    context = {'companies_active': 'active'}
    return render(request, 'companies.html', context)


def faq(request):
    context = {'faq_active': 'active'}
    return render(request, 'faq.html', context)


def about_us(request):
    context = {'about_us_active': 'active'}
    return render(request, 'about-us.html', context)


def register(request):
    context = {'register_active': 'active'}
    return render(request, 'registration.html',  context)
