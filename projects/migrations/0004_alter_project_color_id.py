# Generated by Django 4.0.4 on 2022-06-02 06:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0003_alter_project_color_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='color_id',
            field=models.IntegerField(default=2),
        ),
    ]
