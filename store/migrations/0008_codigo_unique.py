# Generated by Django 2.2.11 on 2020-03-28 06:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0007_empresa_saludo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tipo',
            name='codigo',
            field=models.CharField(max_length=20, unique=True),
        ),
    ]