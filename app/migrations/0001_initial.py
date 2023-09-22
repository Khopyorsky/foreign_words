# Generated by Django 4.2.5 on 2023-09-12 15:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Word',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('russian', models.CharField(max_length=255, verbose_name='Русский')),
                ('english', models.CharField(max_length=255, verbose_name='Английский')),
                ('time_create', models.DateTimeField(auto_now_add=True, verbose_name='Время добавления')),
                ('time_update', models.DateTimeField(auto_now_add=True, verbose_name='Время изменения')),
            ],
            options={
                'verbose_name': 'Слово',
                'verbose_name_plural': 'Слова',
                'ordering': ['russian', 'english'],
            },
        ),
    ]