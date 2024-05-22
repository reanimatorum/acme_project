# Generated by Django 4.2.13 on 2024-05-22 19:40

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('birthday', '0002_birthday_author_birthday_image_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Congratulation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(verbose_name='Текст поздравления')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('birthday', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='congratulations', to='birthday.birthday')),
            ],
            options={
                'ordering': ('created_at',),
            },
        ),
    ]
