# Generated by Django 4.0.8 on 2023-09-21 09:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='title',
            field=models.CharField(default='default title', max_length=255),
            preserve_default=False,
        ),
    ]
