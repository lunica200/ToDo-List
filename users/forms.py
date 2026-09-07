from django import forms  # noqa: I001
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm, UserCreationForm


class LoginUserForm(AuthenticationForm):
    """Форма для авторизации пользователя"""
    username = forms.CharField(label='Логин', 
                               widget=forms.TextInput(attrs={'class': 'form-input'}))
    password = forms.CharField(label='Пароль',
                               widget=forms.PasswordInput(attrs={'class': 'form-input'}))
    
    class Meta:
        model = get_user_model()
        fields = ('username', 'password')


class RegisterUserForm(UserCreationForm):
    """Форма для регистрации пользователя"""
    username = forms.CharField(label='Логин', widget=forms.TextInput(attrs={'class': 'form-input'}))
    password1 = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class': 'form-input'}))
    password2 = forms.CharField(label='Повтор пароля', widget=forms.PasswordInput(attrs={'class': 'form-input'}))
    
    class Meta:
        model = get_user_model()
        fields = ('username', 'email', 'password1', 'password2')
        labels = {'email': 'E-mail'}  # noqa: RUF012
        widgets = {'email': forms.TextInput(attrs={'class': 'form-input'})}  # noqa: RUF012
    
    
    def clean_email(self):
        """Для проверки уникальности email.
        
        :email: Берется из заполненной формы.
        """
        email = self.cleaned_data['email']
        
        if get_user_model().objects.filter(email=email).exists():
            raise forms.ValidationError('Данный E-mail уже зарегистрирован, укажите другой')
        
        return email


class ProfileUserForm(forms.ModelForm):
    """Форма для отображения профиля пользователя"""
    # Нельзя менять
    username = forms.CharField(disabled=True, label='Логин', widget=forms.TextInput(attrs={'class': 'form-input'}))
    email = forms.CharField(disabled=True, label='E-mail', widget=forms.TextInput(attrs={'class': 'form-input'}))
    
    class Meta:
        model = get_user_model()
        fields = ('username', 'email', 'first_name', 'last_name')
        labels = {  # noqa: RUF012
            'first_name': 'Имя',
            'last_name': 'Фамилия'
        }
        widgets = {  # noqa: RUF012
            'first_name': forms.TextInput(attrs={'class': 'form-input'}),
            'last_name': forms.TextInput(attrs={'class': 'form-input'}),
        }


class UserPasswordChangeForm(PasswordChangeForm):
    """Форма для изменения пароля пользователем"""
    old_password = forms.CharField(label="Старый пароль", widget=forms.PasswordInput(attrs={'class': 'form-input'}))
    new_password1 = forms.CharField(label="Новый пароль", widget=forms.PasswordInput(attrs={'class': 'form-input'}))
    new_password2 = forms.CharField(label="Подтверждение пароля", widget=forms.PasswordInput(attrs={'class': 'form-input'}))