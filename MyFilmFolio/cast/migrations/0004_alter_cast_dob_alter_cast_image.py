# Generated by Django 5.0.3 on 2024-05-03 06:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cast', '0003_alter_cast_image_alter_cast_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cast',
            name='DoB',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='cast',
            name='Image',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
