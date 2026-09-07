from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import F
from django.shortcuts import render
from django.views.generic import CreateView, DeleteView, UpdateView

from todoapp.forms import TaskForm
from todoapp.models import AllTask, TimeCategory

# Содержит все категории
categories = TimeCategory.objects.all()

# Представления для изменения задач
class CreateNewTask(LoginRequiredMixin, CreateView):
    """Для отображения страницы создания новой задачи.
    
    :form_class: Откуда берет параметры для создания формы.
    :template_name: какой шаблон для страницы использует.
    """
    form_class = TaskForm
    template_name = 'todoapp/new_task.html'
    
    def form_valid(self, form):
        """Атоматически привязывает задачу к текущему пользователю."""
        
        form.instance.user = self.request.user
        return super().form_valid(form)


class EditTask(LoginRequiredMixin, UpdateView):
    """Для отображения страницы изменения задачи.
    
    :model: Из какой модели будет брать данные.
    :fields: Какие значения будут доступны для изменения.
    :template_name: Какой шаблон для страницы использует.
    """
    model = AllTask
    fields = ('name', 'time_category', 'deadline', 'status', 'description')    
    template_name = 'todoapp/edit_task.html'
    
    def get_form(self, form_class=None):
        """Меняет начальные отображения time_category и status.
        
        :form_class: TaskForm.
        """
        form = super().get_form(form_class)
        form.fields['time_category'].empty_label = None
        form.fields['status'].empty_label = None
        
        return form
    
    
    def get_queryset(self):
        """Словарь задач только этого пользователя."""
        
        return AllTask.objects.filter(user=self.request.user)


class DeleteTask(LoginRequiredMixin, DeleteView):
    """Для удаления задачи.
    
    :model: Из какой модели удалить задачу.
    """
    model = AllTask
    
    def get_success_url(self):
        """Куда перенаправит. Ссылку берет из AllTask."""
        return self.object.get_absolute_url()
    
    
    def get_queryset(self):
        return AllTask.objects.filter(user=self.request.user)
    

# Представления для отображения категорий
@login_required
def show_first_category(request):
    """Показывает все задачи.
    
    :tasks_by_category: Все задачи, сортированные по статусу и дедлайну.
    """
    tasks_by_category = AllTask.objects.filter(user=request.user).order_by('status', F('deadline').asc(nulls_last=True))  
    
    data = {
        'categories': categories,
        'tasks_by_category': tasks_by_category
    }
    
    return render(request, 'todoapp/category.html', data)


@login_required
def show_category(request, category_slug):
    """Показывает задачи в зависимости от слага.
    
    :selected_slug: Слаг из адресной строки.
    :tasks_by_category: Задачи одной категори, сортированные по статусу и дедлайну.
    """
    selected_slug = category_slug
    tasks_by_category = AllTask.objects.filter(user=request.user, time_category__slug=category_slug).order_by('status', F('deadline').asc(nulls_last=True))
    
    data = {
        'categories': categories,
        'tasks_by_category': tasks_by_category,
        'selected_slug': selected_slug
    }
    
    return render(request, 'todoapp/category.html', data)


def custom_404(request, exception):
    """Для отображения страницы 404"""
    return render(request, 'todoapp/page_404.html', status=404)