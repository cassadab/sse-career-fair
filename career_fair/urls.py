from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('companies/', views.companies, name='companies'),
    path('faq/', views.faq, name='faq'),
    path('about/', views.about_us, name='about'),
    path('register/', views.RegisterView.as_view(), name='register'),
    # path('thank-you/', views.ThankYouView.as_view(), name='thank-you'),
]
