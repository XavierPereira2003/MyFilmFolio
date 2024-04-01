# Generated by Django 5.0.3 on 2024-04-01 15:47

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("movies", "0002_genre_remove_movies_genre_movies_genre"),
    ]

    operations = [
        migrations.AddField(
            model_name="movies",
            name="slug",
            field=models.SlugField(
                default=django.utils.timezone.now, max_length=255, unique=True
            ),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name="movies",
            name="genre",
            field=models.ManyToManyField(related_name="movies", to="movies.genre"),
        ),
    ]
