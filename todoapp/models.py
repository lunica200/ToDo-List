from autoslug import AutoSlugField
from autoslug.settings import slugify
from django.db import models
from django.urls import reverse
from transliterate import translit

from ToDo import settings


def custom_slugify(value):
    """Транслитерация русских букв в латиницу"""
    latin_value = translit(value, 'ru', reversed=True)
    
    return slugify(latin_value)


# Create your models here.
class AllTask(models.Model):
    """Модель для всех задач"""
    name = models.CharField(verbose_name='Название', max_length=100, editable=True)
    slug = AutoSlugField(verbose_name='Слаг', 
                        populate_from='name', 
                        max_length=100, 
                        unique=True, 
                        db_index=True, 
                        slugify=custom_slugify,
                        always_update=True,
                        null=True, blank=True
                        )
    description = models.TextField(verbose_name='Описание', max_length=250, blank=True)
    deadline = models.DateField(verbose_name='Дедлайн', blank=True, null=True)
    created_time = models.DateField(verbose_name='Дата создания', auto_now_add=True)
    
    # Связанные значения
    time_category = models.ForeignKey('TimeCategory', verbose_name='Категория времени', default=1, on_delete=models.CASCADE)
    status = models.ForeignKey('Status', verbose_name='Статус выполнения', default=2, on_delete=models.SET_DEFAULT)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name='Пользователь', null=True, blank=True, on_delete=models.CASCADE)
    
    class Meta:
        verbose_name = 'Задача'
        verbose_name_plural = 'Задачи'
            
    
    def __str__(self):
        return self.name
    
    
    def get_absolute_url(self):
        return reverse("category", kwargs={"category_slug": self.time_category.slug})  
    


class TimeCategory(models.Model):
    """Модель для категорий"""
    name = models.CharField(verbose_name='Категория')
    slug = AutoSlugField(verbose_name='Слаг', 
                        populate_from='name', 
                        max_length=100, 
                        unique=True, 
                        db_index=True, 
                        slugify=custom_slugify,
                        always_update=True
                        )
    
    
    class Meta:
        verbose_name = 'Категория по времени'
        verbose_name_plural = 'Категории по времени'
       
       
    def __str__(self):
        return self.name
    
    
    def get_absolute_url(self):
        return reverse("category", kwargs={"category_slug": self.slug})
    
    

class Status(models.Model):
    """Модель для статусов задачи"""
    name = models.CharField(verbose_name='Название')
    slug = AutoSlugField(verbose_name='Слаг',
                         populate_from = 'name',
                         max_length=100,
                         unique=True,
                         db_index=True,
                         slugify=custom_slugify,
                         always_update=True
                         )
    
    
    class Meta:
        verbose_name = 'Статус'
        verbose_name_plural = 'Статус'
        
    def __str__(self):
        return self.name