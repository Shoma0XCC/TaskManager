import django_filters
from .models import Task

class TaskFilter(django_filters.FilterSet):
    status = django_filters.ChoiceFilter(choices=Task.STATUS_CHOICES)  # Фильтр по статусу

    class Meta:
        model = Task
        fields = ['status']