from django import forms
from career_fair.models import Student
from career_fair.models import Major


class RegistrationForm(forms.ModelForm):
    name = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'form-control item'
        }
    ))
    email = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'form-control item'
        }
    ))
    major = forms.ModelChoiceField(queryset=Major.objects.all(), widget=forms.Select(
        attrs={
            'class': 'form-control item'
        }
    ))
    graduation_year = forms.IntegerField(widget=forms.TextInput(
        attrs={
            'class': 'form-control item'
        }
    ))
    resume_link = forms.CharField(widget=forms.URLInput(
        attrs={
            'class': 'form-control item'
        }
    ), required=False, label="Resume link (optional):")

    class Meta:
        model = Student
        fields = ('name', 'email', 'major', 'graduation_year', 'resume_link')
