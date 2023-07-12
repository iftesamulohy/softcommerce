# Generated by Django 4.2 on 2023-05-11 20:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('utilities', '0013_utilities'),
    ]

    operations = [
        migrations.AddField(
            model_name='utilities',
            name='menu',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='utilities',
            name='social',
            field=models.ManyToManyField(to='utilities.button'),
        ),
    ]