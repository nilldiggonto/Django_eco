# Generated by Django 2.1.4 on 2019-01-24 16:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('billing', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address_type', models.CharField(choices=[('billing', 'Billing'), ('shipping', 'Shipping')], max_length=120)),
                ('address_line_1', models.CharField(max_length=120)),
                ('address_line_2', models.CharField(max_length=120)),
                ('country', models.CharField(default='BD', max_length=120)),
                ('city', models.CharField(max_length=120)),
                ('state', models.CharField(max_length=120)),
                ('postal_code', models.CharField(max_length=120)),
                ('billing_profile', models.ForeignKey(on_delete='DO_NOTHING', to='billing.BillingProfile')),
            ],
        ),
    ]
