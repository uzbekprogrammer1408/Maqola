# Generated by Django 3.2.9 on 2021-12-19 07:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Articles',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Mavzu')),
                ('matn', models.TextField(verbose_name='Maqola matni')),
                ('muallif', models.CharField(max_length=30, verbose_name='Maqola muallifi')),
                ('sana', models.DateField(verbose_name='Nashr sanasi')),
            ],
        ),
    ]