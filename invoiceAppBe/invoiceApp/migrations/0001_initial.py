# Generated by Django 4.1.2 on 2022-10-22 22:13

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('username', models.CharField(max_length=15, unique=True, verbose_name='Username')),
                ('password', models.CharField(max_length=256, verbose_name='Password')),
                ('name', models.CharField(max_length=30, verbose_name='Name')),
                ('lastname', models.CharField(max_length=30, verbose_name='LastName')),
                ('city', models.CharField(max_length=30, verbose_name='City')),
                ('address', models.CharField(max_length=30, verbose_name='Address')),
                ('email', models.EmailField(max_length=100, verbose_name='Email')),
                ('rol', models.CharField(blank=True, max_length=30, null=True, verbose_name='Rol')),
                ('cellphone', models.CharField(max_length=30, verbose_name='CellPhone')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Empleado',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('contrato', models.CharField(max_length=30, verbose_name='contrato')),
                ('area', models.CharField(max_length=30, verbose_name='area')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Proveedor',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=30, verbose_name='nombre')),
                ('fecha', models.CharField(max_length=30, verbose_name='fecha')),
                ('costo', models.FloatField()),
                ('empleado', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='invoiceApp.empleado')),
            ],
        ),
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=30, verbose_name='nombre')),
                ('cantidad', models.IntegerField()),
                ('pais', models.CharField(max_length=30, verbose_name='pais')),
                ('precioU', models.FloatField()),
                ('proveedor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='invoiceApp.proveedor')),
            ],
        ),
        migrations.CreateModel(
            name='Factura',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('mPago', models.CharField(max_length=30, verbose_name='mPago')),
                ('costoTotal', models.FloatField(default=0)),
                ('cliente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='invoiceApp.cliente')),
            ],
        ),
        migrations.CreateModel(
            name='Compra',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cantidad', models.IntegerField()),
                ('precioTotal', models.FloatField()),
                ('factura', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='invoiceApp.factura')),
                ('producto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='invoiceApp.producto')),
            ],
        ),
    ]
