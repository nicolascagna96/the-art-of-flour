# Generated by Django 3.2.16 on 2022-10-26 14:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_auto_20221026_1350'),
    ]

    operations = [
        migrations.AddField(
            model_name='recipes',
            name='email',
            field=models.EmailField(blank=True, max_length=254),
        ),
    ]