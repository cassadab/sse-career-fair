from django.shortcuts import render


def index(request):
    return render(request, 'index.html')


def companies(request):
    return render(request, 'companies.html')


def faq(request):
    return render(request, 'faq.html')
