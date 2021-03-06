# Generated by Django 3.1.7 on 2021-03-30 05:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Members',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('userName', models.CharField(max_length=100)),
                ('passWord', models.CharField(max_length=100)),
                ('name', models.CharField(max_length=200)),
                ('email', models.EmailField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='order_products',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Member_id', models.IntegerField()),
                ('product_id', models.IntegerField()),
                ('product_price', models.FloatField()),
                ('total', models.IntegerField()),
                ('order_date', models.DateField()),
                ('order_status', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='product_cmt',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Member_id', models.IntegerField()),
                ('product_id', models.IntegerField()),
                ('cmt', models.CharField(max_length=2000)),
            ],
        ),
        migrations.CreateModel(
            name='Products',
            fields=[
                ('product_id', models.AutoField(primary_key=True, serialize=False)),
                ('product_name', models.CharField(max_length=100)),
                ('product_price', models.FloatField()),
                ('product_quantity', models.IntegerField()),
                ('product_cmt', models.CharField(max_length=1000)),
            ],
        ),
    ]
