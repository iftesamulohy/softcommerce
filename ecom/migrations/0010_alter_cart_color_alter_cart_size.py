# Generated by Django 4.2 on 2023-05-20 04:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ecom', '0009_order_date_cuopone_order_used_cuopone'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cart',
            name='color',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='ecom.color'),
        ),
        migrations.AlterField(
            model_name='cart',
            name='size',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='ecom.size'),
        ),
    ]
