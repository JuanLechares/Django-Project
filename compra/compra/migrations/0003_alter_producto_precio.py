# Generated by Django 5.0.3 on 2024-04-02 22:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('compra', '0002_alter_producto_options_alter_producto_table'),
    ]

    operations = [
        migrations.AlterField(
            model_name='producto',
            name='precio',
            field=models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Precio'),
        ),
    ]
