from django.db import models

# Create your models here.

class Category(models.Model):
    class Meta:
        db_table = "categories"
    def __str__(self):
        return self.name
    name = models.CharField("카테고리 이름", max_length=50)


class Item(models.Model):
    class Meta:
        db_table = "items"
    def __str__(self):
        return self.name
    name = models.CharField("이름", max_length=50)
    thumnail = models.URLField(max_length=300, null=False, default='')
    category = models.ForeignKey(Category, verbose_name="카테고리", on_delete=models.SET_NULL)
    orders = models.ManyToManyField('Order', verbose_name="장바구니", through='ItemOrder', related_name="item_orders")

class ItemOrder(models.Model):
    count = models.IntegerField("수량")

class Order(models.Model):
    class Meta:
        db_table = "orders"
    def __str__(self):
        return self.name
    delivery_adrress = models.CharField("주소", max_length=200)
    order_date = models.DateTimeField("주문시각", )
