from django.urls import path
from . import views

app_name = 'product'
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:lesson_id>', views.single_lesson, name='single_lesson')
]
