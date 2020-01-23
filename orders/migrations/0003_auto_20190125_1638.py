# Generated by Django 2.1.4 on 2019-01-25 10:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('addresses', '0001_initial'),
        ('orders', '0002_auto_20190124_0123'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='billing_address',
            field=models.ForeignKey(blank=True, null=True, on_delete='DO_NOTHING', related_name='billing_address', to='addresses.Address'),
        ),
        migrations.AddField(
            model_name='order',
            name='shipping_address',
            field=models.ForeignKey(blank=True, null=True, on_delete='DO_NOTHING', related_name='shipping_address', to='addresses.Address'),
        ),
    ]
