from django.contrib.auth import get_user_model, logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import (
    LoginView,
    PasswordChangeDoneView,
    PasswordChangeView,
    PasswordResetCompleteView,
    PasswordResetConfirmView,
    PasswordResetDoneView,
    PasswordResetView,
)
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView

from .forms import (
    LoginUserForm,
    ProfileUserForm,
    RegisterUserForm,
    UserPasswordChangeForm,
)


# Для авторизации пользователя
class LoginUser(LoginView):
    """Для отображения страницы авторизации пользователя.
    
    :form_class: Откуда берет параметры для создания формы.
    :template_name: Какой шаблон для страницы использует.
    """
    form_class = LoginUserForm
    template_name = 'users/login.html'


def logout_user(request):
    """Для выхода из системы и переноса на страницу авторизации."""
    logout(request)
    return redirect('users:login')


# Для регистрации пользователя
class RegisterUser(CreateView):
    """Для отображения страницы регистрации пользователя.
    
    :form_class: Откуда берет параметры для создания формы.
    :template_name: Какой шаблон для страницы использует.
    :success_url: Куда перенесет при успешной регистрации.
    """
    form_class = RegisterUserForm
    template_name = 'users/register.html'
    success_url = reverse_lazy('users:register_done')
    
    
def register_done(request):
    """Для отображения страницы при успешной регистрации пользователя."""
    return render(request, 'users/register_done.html')


# Для профиля
class ProfileUser(LoginRequiredMixin, UpdateView):
    """Для отображения страницы профиля пользователя.
    
    :model: Из какой модели будет брать данные.
    :form_class: Откуда берет параметры для создания формы.
    :template_name: Какой шаблон для страницы использует.
    """
    model = get_user_model()
    form_class = ProfileUserForm
    template_name = 'users/profile.html'


    def get_success_url(self):
        """Куда перенесет при успешном изменении данных в профиле."""
        return reverse_lazy('users:profile')   
    
    
    def get_object(self, queryset=None):
        """Чтобы показывался профиль авторизованного пользователя, без его отображения в адресной строке."""
        return self.request.user
    

# Для изменения пароля
class UserPasswordChange(PasswordChangeView):
    """Для отображения страницы изменения пароля пользователя.
    
    :form_class: Откуда берет параметры для создания формы.
    :template_name: Какой шаблон для страницы использует.
    :success_url: Куда перенесет при успешной смене пароля.
    """
    form_class = UserPasswordChangeForm
    template_name = 'users/password_change.html'
    success_url = reverse_lazy('users:password_change_done')
    

class UserPasswordChangeDone(PasswordChangeDoneView):
    """Для отображения страницы при успешной смене пароля пользователя.
        
    :template_name: Какой шаблон для страницы использует.
    """
    template_name = 'users/password_change_done.html'
    
    
# Для восстановления пароля
class UserPasswordReset(PasswordResetView):
    """Для отображения страницы сброса пароля пользователя.
        
    :template_name: Какой шаблон для страницы использует.
    :email_template_name: Какой шаблон для email сообщения использует.
    :success_url: Куда перенесет при успешной смене пароля.
    """
    template_name = "users/password_reset.html"
    email_template_name = "users/password_reset_email.html"
    success_url = reverse_lazy("users:password_reset_done")
    
    
class UserPasswordResetDone(PasswordResetDoneView):
    """Для отображения страницы после успешного сброса пароля пользователя.
        
    :template_name: Какой шаблон для страницы использует.
    """
    template_name = "users/password_reset_done.html"
    

class UserPasswordResetConfirm(PasswordResetConfirmView):
    """Для отображения страницы при переходе по ссылке из email и создания нового пароля.
        
    :template_name: Какой шаблон для страницы использует.
    :success_url: Куда перенесет при успешной смене пароля.
    """
    template_name = "users/password_reset_confirm.html"
    success_url = reverse_lazy("users:password_reset_complete")    
    
    
class UserPasswordResetComplete(PasswordResetCompleteView):
    """Для отображения страницы после успешного создания пароля пользователя.
        
    :template_name: Какой шаблон для страницы использует.
    """
    template_name = "users/password_reset_complete.html"