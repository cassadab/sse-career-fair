from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('companies/', views.companies, name='companies'),
    path('faq/', views.faq, name='faq'),
    path('about/', views.about_us, name='about'),
    path('register/', views.register, name='register'),
]
