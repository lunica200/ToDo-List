from django import forms

from .models import AllTask, TimeCategory


class TaskForm(forms.ModelForm):
    """Форма для добавления новой задачи и изменения существующей.
    
    :model: Из какой модели будет брать данные.
    :fields: Какие значения будут доступны для изменения.
    """
    
    time_category = forms.ModelChoiceField(queryset=TimeCategory.objects.all(), initial='Без категории', label="Категория времени")
    
    class Meta:
        model = AllTask
        fields = ('name', 'time_category', 'deadline', 'description')
        widgets = {'deadline': forms.DateInput(attrs={'type': 'date'})}  # noqa: RUF012
