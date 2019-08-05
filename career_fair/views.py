from django.shortcuts import render, redirect
from django.views.generic import TemplateView

from career_fair.models import Company
from career_fair.models import FAQ
from .forms import RegistrationForm


def index(request):
    context = {'home_active': 'active'}
    return render(request, 'index.html', context)


def companies(request):
    context = {'companies_active': 'active', 'companies': Company.objects.all()}
    return render(request, 'companies.html', context)


def faq(request):
    context = {'faq_active': 'active', 'faqs': FAQ.objects.all()}
    return render(request, 'faq.html', context)


def about_us(request):
    context = {'about_us_active': 'active'}
    return render(request, 'about-us.html', context)


class ThankYouView(TemplateView):

    def get(self, request, *args, **kwargs):
        return render(request, 'thank-you.html')


class RegisterView(TemplateView):
    template_name = 'registration.html'

    def get(self, request, *args, **kwargs):
        form = RegistrationForm()
        context = {'register_active': 'active', 'form': form}
        return render(request, 'registration.html', context)

    def post(self, request):
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            # TODO What if email is already in the db
            context = {'email': form.cleaned_data['email']}
            return render(request, 'thank-you.html', context)
        return render(request, 'registration.html')
