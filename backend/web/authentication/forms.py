from django.contrib.auth.forms import AuthenticationForm



class MyAuthForm(AuthenticationForm):
    def __init__(self, request = None, *args, **kwargs):
        super().__init__(request, *args, **kwargs)

        self.fields['username'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Имя пользователя',
            'required': True
        })
        self.fields['username'].label = 'Имя пользователя'

        self.fields['password'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Пароль',
            'required': True
        })