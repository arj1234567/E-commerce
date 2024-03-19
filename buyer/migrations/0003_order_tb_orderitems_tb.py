# Generated by Django 5.0.1 on 2024-02-05 06:12

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('buyer', '0002_cart_tb'),
        ('seller', '0003_alter_product_tb_details_alter_product_tb_stock'),
    ]

    operations = [
        migrations.CreateModel(
            name='order_tb',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=20)),
                ('Address', models.CharField(max_length=20)),
                ('Phone', models.CharField(max_length=20)),
                ('Orderdate', models.CharField(max_length=20)),
                ('Ordertime', models.CharField(max_length=20)),
                ('Status', models.CharField(default='pending', max_length=20)),
                ('Grandtotal', models.IntegerField()),
                ('Buyer_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='buyer.buyer_tb')),
            ],
        ),
        migrations.CreateModel(
            name='orderItems_tb',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Quantity', models.IntegerField()),
                ('Price', models.IntegerField()),
                ('Buyer_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='buyer.buyer_tb')),
                ('Order_Id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='buyer.order_tb')),
                ('Product_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='seller.product_tb')),
            ],
        ),
    ]
