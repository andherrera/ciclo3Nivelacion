# Generated by Django 4.1.2 on 2022-10-22 22:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('invoiceApp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='email',
        ),
    ]