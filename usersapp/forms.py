from django import forms
from django.contrib.auth import (
    authenticate,
    get_user_model

)

User = get_user_model()


class UserLoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control ', 'type':'text',
                                'placeholder': 'Username or email', 'id':'username',
                                 }))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'type':'password',
                                'placeholder': 'Password', 'id':'password',}))

    def clean(self, *args, **kwargs):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')

        if username and password:
            user = authenticate(username=username, password=password)
            if not user:
                raise forms.ValidationError('This user does not exist')
            if not user.check_password(password):
                raise forms.ValidationError('Incorrect password')
            if not user.is_active:
                raise forms.ValidationError('This user is not active')
        return super(UserLoginForm, self).clean(*args, **kwargs)


class UserRegisterForm(forms.ModelForm):
    first_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control ', 'type':'text',
                                 'placeholder': 'First Name', 'id':'first_name', 'name':'first_name','required':False, 'help_text':'Optional.',
                                  }), label='first Name')
    last_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control ', 'type':'text',
                                'placeholder': 'Last Nmae', 'id':'last_name', 'name':'last_name',
                                 'required':False, 'help_text':'Optional.',}), label='Last Name')
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control ', 'type':'text',
                                'placeholder': 'Username', 'id':'username','name':'username',
                                 }), label='username')
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control ', 'type':'email',
                                'placeholder': 'email', 'id':'email', 'name':'email',
                                 }), label='Email address')
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control ', 'type':'password',
                                'placeholder': 'password', 'id':'password1', 'name':'password1'
                                 }))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control ', 'type':'password',
                                'placeholder': 'confirm password', 'id':'password2', 'name':'password1',
                                 }))

    class Meta:
        model = User
        fields = [
            'first_name',
            'last_name',
            'username',
            'email',
            'password1',
            'password2',
        ]

    def clean(self, *args, **kwargs):
        cleaned_data = super(UserRegisterForm, self).clean(*args, **kwargs)
        first_name = self.cleaned_data.get('first_name')
        last_name = self.cleaned_data.get('last_name')
        username = cleaned_data.get('username')
        email = self.cleaned_data.get('email')
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')
        if password1 != password2:
            raise forms.ValidationError("Password must match")
        email_qs = User.objects.filter(email=email)
        if email_qs.exists():
            raise forms.ValidationError(
                "This email has already been registered")
        username_qs = User.objects.filter(username=username)
        if username_qs.exists():
            raise forms.validationError(
                "This username already taken"
            )
        if ('@', '.', '-', '+') in username:
            raise forms.validationError('username', 'Symbols @/./-/+ are not allowed in username.')
        return cleaned_data
