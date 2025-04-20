from django import forms

from Subject.models import User


class RegistrationForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['email', 'username', 'password', 'password_check', 'agree_to_terms', 'mailing']
        labels = {
            "username": "Логин",
            "email": "Почта",
            "password": "Пароль",
            "agree_to_terms": "Соглашение с правилами сайта",
            "mailing": "Согласие на рассылку"
        }
        widgets = {
            'username': forms.TextInput(attrs={
                'class': "form-control",
                'placeholder': "Логин"
            }),
            'first_name': forms.TextInput(attrs={
                'class': "form-control",
                'placeholder': "Имя"
            }),
            'last_name': forms.TextInput(attrs={
                'class': "form-control",
                'placeholder': "Фамилия"
            }),
            'patronymic': forms.TextInput(attrs={
                'class': "form-control",
                'placeholder': "Отчество"
            }),
            'email': forms.EmailInput(attrs={
                'class': "form-control",
                'placeholder': "Почта"
            }),
            'password': forms.PasswordInput(attrs={
                'class': "form-control",
                'placeholder': "Пароль"
            }),
            'agree_to_terms': forms.CheckboxInput(attrs={
                'class': "form-check-input"
            }),
        }

    password_check = forms.CharField(label='Подтверждение пароля', widget=forms.PasswordInput(attrs={
        'placeholder': 'Подтвердите пароль',
        'class': 'form-control'
        }))