# Generated by Django 5.1.2 on 2024-11-20 09:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("store", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="product",
            name="slug",
            field=models.SlugField(default=1, max_length=200, unique=True),
            preserve_default=False,
        ),
    ]
