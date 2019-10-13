from django.db import models


# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=512, verbose_name="Kategori Adı")
    description = models.TextField(null=True, blank=True, verbose_name="Açıklama")
    parent = models.ForeignKey("Category", null=True, blank=True, on_delete=models.CASCADE, verbose_name="Üst Kategori")

    def __str__(self):
        return self.name


class Brand(models.Model):
    name = models.CharField(max_length=512, verbose_name="Marka Adı")
    description = models.TextField(null=True, blank=True, verbose_name="Açıklama")
    logo = models.ImageField(upload_to='images/brand', null=True, blank=True)

    def __str__(self):
        return self.name


CURRENCY = (
    (1, "GBP"),
    (2, "Dolar"),
    (3, "Euro"),
    (3, "Turkish Lira"),
)
STOCK_TRACKING = ((1, "Stok Takip Edilsin"), (0, 'Stoklar Takip Edilmesin'))


class Product(models.Model):
    # urunun adı
    name = models.CharField(max_length=512, null=True, blank=True, verbose_name="Product Name")
    code = models.CharField(max_length=512, verbose_name="Code")
    barcode = models.CharField(max_length=64, verbose_name="Barcode")
    brand = models.ForeignKey(Brand, null=True, blank=True, on_delete=models.SET_NULL, related_name="product_brand",
                              verbose_name="Marka")
    description = models.TextField(null=True, blank=True, verbose_name="Açıklama")
    weight = models.CharField(max_length=512, verbose_name="Ağırlık")
    categories = models.ManyToManyField(Category, blank=True, related_name="product_categories",
                                        verbose_name="Kategoriler")
    # Fiyat
    buying_price = models.FloatField(default=0, verbose_name="Buying Price")
    selling_price = models.FloatField(default=0, verbose_name="Selling Price")
    special_price = models.FloatField(default=0, verbose_name="Special Price")
    vat = models.FloatField(default=8, verbose_name="VAT")
    currency = models.IntegerField(choices=CURRENCY, default=1, verbose_name="Currency")

    stock_tracking = models.IntegerField(choices=STOCK_TRACKING, default=1, verbose_name="Stokar takip edilsinmi")
    qty_alert = models.IntegerField(blank=True, null=True, verbose_name="Stok Uyarısı")
    created_at = models.DateTimeField(auto_now_add=True)
    # son guncelleme zamani
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
