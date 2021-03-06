# Generated by Django 3.0.6 on 2020-08-25 08:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Fabricante',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=42)),
                ('pais', models.CharField(max_length=42)),
                ('sitioweb', models.URLField()),
            ],
        ),
        migrations.CreateModel(
            name='Productos_Medicinales',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('precio', models.CharField(max_length=20)),
                ('caracteristicas', models.TextField()),
                ('imagen', models.ImageField(upload_to='productos')),
            ],
        ),
        migrations.CreateModel(
            name='Semillas',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('precio', models.CharField(max_length=20)),
                ('caracteristicas', models.TextField()),
                ('detalles', models.TextField()),
                ('imagen', models.ImageField(upload_to='productos')),
            ],
        ),
        migrations.CreateModel(
            name='Suplementos',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('precio', models.CharField(max_length=20)),
                ('caracteristicas', models.TextField()),
                ('detalles', models.TextField()),
                ('imagen', models.ImageField(upload_to='productos')),
            ],
        ),
        migrations.CreateModel(
            name='Herramientas',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('precio', models.CharField(max_length=20)),
                ('caracteristicas', models.TextField()),
                ('especificiaciones', models.TextField()),
                ('imagen', models.ImageField(upload_to='productos')),
                ('fabricante', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pic.Fabricante')),
            ],
        ),
    ]
