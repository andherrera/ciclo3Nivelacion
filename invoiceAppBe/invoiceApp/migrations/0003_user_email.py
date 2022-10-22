# Generated by Django 4.1.2 on 2022-10-22 22:23

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('invoiceApp', '0002_remove_user_email'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='email',
            field=models.EmailField(default=django.utils.timezone.now, max_length=100, verbose_name='Email'),
            preserve_default=False,
        ),
    ]