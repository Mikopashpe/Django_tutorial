# Generated by Django 4.0.5 on 2022-07-25 05:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crm', '0002_alter_order_options_alter_order_order_dt_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='order_dt',
            field=models.DateTimeField(blank=True, null=True, verbose_name='Дата'),
        ),
    ]
