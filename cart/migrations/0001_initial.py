# Generated by Django 4.2.4 on 2023-09-02 18:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('inventory', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product', models.CharField(max_length=32)),
                ('total', models.FloatField()),
                ('number_of_products', models.PositiveIntegerField()),
                ('shipping_cost', models.FloatField()),
                ('payment_options', models.CharField(max_length=20)),
                ('discount', models.FloatField()),
                ('products', models.ManyToManyField(to='inventory.product')),
            ],
        ),
    ]
