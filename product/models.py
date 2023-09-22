from django.db import models
from django.utils import timezone


class Product(models.Model):
    title = models.CharField(max_length=255)
    owner = models.CharField(max_length=255)
    creared_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title


class Lesson(models.Model):
    title = models.CharField(max_length=255)
    url_path = models.TextField(default='')
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    owner = models.CharField(max_length=255)
    during_veiw = models.IntegerField()

    def __str__(self):
        return self.title


class User(models.Model):
    username = models.CharField(
        unique=True,
        max_length=50,
        verbose_name='Nikname',
        help_text='Enter your niknmae'
    )
    first_name = models.CharField(
        max_length=50,
        verbose_name='Имя',
        help_text='Введите имя',
    )
    last_name = models.CharField(
        max_length=50,
        verbose_name='Фамилия',
        help_text='Введите фамилию',
    )
    email = models.EmailField(
        max_length=50,
        blank=False,
        unique=True,
        verbose_name='Адрес электронной почты',
        help_text='Укажите адрес электронной почты',
    )

    class Meta:
        ordering = ('username',)
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

    def __str__(self) -> str:
        return self.username


class LessonView(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE)
    time_view = models.DateTimeField(default=timezone.now)
    status_view = models.BooleanField(default=False)
    viewed_duration = models.IntegerField(default=0)

    def save(self, *args, **kwargs):
        if self.viewed_duration >= (self.lesson.during_veiw * 0.8):
            self.status = True
        else:
            self.status = False
        super().save(*args, **kwargs)

    def __str__(self) -> str:
        return self.user
