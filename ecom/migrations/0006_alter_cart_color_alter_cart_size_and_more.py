# Generated by Django 4.2 on 2023-05-07 16:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ecom', '0005_cart_vendor_wishlist_vendor_orderedproduct'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cart',
            name='color',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ecom.color'),
        ),
        migrations.AlterField(
            model_name='cart',
            name='size',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ecom.size'),
        ),
        migrations.AlterField(
            model_name='orderedproduct',
            name='color',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ecom.color'),
        ),
        migrations.AlterField(
            model_name='orderedproduct',
            name='size',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ecom.size'),
        ),
        migrations.AlterField(
            model_name='wishlist',
            name='color',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ecom.color'),
        ),
        migrations.AlterField(
            model_name='wishlist',
            name='size',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ecom.size'),
        ),
    ]
