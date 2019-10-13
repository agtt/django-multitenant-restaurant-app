# Generated by Django 2.2.6 on 2019-10-13 17:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Brand',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=512, verbose_name='Marka Adı')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Açıklama')),
                ('logo', models.ImageField(blank=True, null=True, upload_to='images/brand')),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=512, verbose_name='Kategori Adı')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Açıklama')),
                ('parent', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='product.Category', verbose_name='Üst Kategori')),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=512, null=True, verbose_name='Product Name')),
                ('code', models.CharField(max_length=512, verbose_name='Code')),
                ('barcode', models.CharField(max_length=64, verbose_name='Barcode')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Açıklama')),
                ('weight', models.CharField(max_length=512, verbose_name='Ağırlık')),
                ('buying_price', models.FloatField(default=0, verbose_name='Buying Price')),
                ('selling_price', models.FloatField(default=0, verbose_name='Selling Price')),
                ('special_price', models.FloatField(default=0, verbose_name='Special Price')),
                ('vat', models.FloatField(default=8, verbose_name='VAT')),
                ('currency', models.IntegerField(choices=[(1, 'GBP'), (2, 'Dolar'), (3, 'Euro'), (3, 'Turkish Lira')], default=1, verbose_name='Currency')),
                ('stock_tracking', models.IntegerField(choices=[(1, 'Stok Takip Edilsin'), (0, 'Stoklar Takip Edilmesin')], default=1, verbose_name='Stokar takip edilsinmi')),
                ('qty_alert', models.IntegerField(blank=True, null=True, verbose_name='Stok Uyarısı')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('brand', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='product_brand', to='product.Brand', verbose_name='Marka')),
                ('categories', models.ManyToManyField(blank=True, related_name='product_categories', to='product.Category', verbose_name='Kategoriler')),
            ],
        ),
    ]
