# Generated by Django 4.0.4 on 2022-06-02 06:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('routines', '0004_alter_routine_day'),
    ]

    operations = [
        migrations.AlterField(
            model_name='routine',
            name='day',
            field=models.CharField(default='Thursday', max_length=10),
        ),
    ]