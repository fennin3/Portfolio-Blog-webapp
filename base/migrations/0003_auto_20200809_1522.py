# Generated by Django 3.0.8 on 2020-08-09 15:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0002_port_project'),
    ]

    operations = [
        migrations.AlterField(
            model_name='portfolio',
            name='technologies',
            field=models.ManyToManyField(to='base.Port_Project'),
        ),
    ]
