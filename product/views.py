from django.shortcuts import render, get_object_or_404
from .models import Lesson, Product, LessonView


def index(request):
    lessons = Lesson.objects.all()
    products = Product.objects.all()
    return render(request, 'product/lessons.html', {'lessons': lessons, 'products': products})


def single_lesson(request, lesson_id):
    lesson = get_object_or_404(Lesson, pk=lesson_id)
    lesson_views = LessonView.objects.filter(lesson_id=lesson_id)
    return render(request, 'product/single_lesson.html', {'lesson': lesson, 'lesson_views': lesson_views})
