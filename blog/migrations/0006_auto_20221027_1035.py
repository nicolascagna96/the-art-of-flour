# Generated by Django 3.2.16 on 2022-10-27 10:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_recipes_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipes',
            name='body',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='recipes',
            name='image',
            field=models.ImageField(blank=True, upload_to=''),
        ),
    ]
