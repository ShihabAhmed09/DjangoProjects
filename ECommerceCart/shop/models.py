from django.db import models


# Create your models here.
# Model for Product
class Product(models.Model):
    product_id = models.AutoField
    product_name = models.CharField(max_length=100)
    category = models.CharField(max_length=50, default="")
    subcategory = models.CharField(max_length=50, default="")
    price = models.FloatField(default=0)
    description = models.CharField(max_length=500)
    publish_date = models.DateField()
    image = models.ImageField(upload_to="shop/images", default="")

    # this function returns product name in database, otherwise database will show Product Object(1,2,...) in database
    def __str__(self):
        return self.product_name


# Model for Contact
class Contact(models.Model):
    msg_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100, default="")
    phone = models.CharField(max_length=50, default="")
    description = models.CharField(max_length=500, default="")

    def __str__(self):
        return self.name


# Model for Order
class Order(models.Model):
    order_id = models.AutoField(primary_key=True)
    items_json = models.CharField(max_length=5000)
    amount = models.FloatField(max_length=100, default=0)
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100, default="")
    phone = models.CharField(max_length=50, default="")
    address = models.CharField(max_length=200, default="")
    city = models.CharField(max_length=100, default="")
    state = models.CharField(max_length=100, default="")
    zip_code = models.CharField(max_length=50, default="")

    # def __str__(self):
    #     return self.name


class OrderUpdate(models.Model):
    update_id = models.AutoField(primary_key=True)
    order_id = models.IntegerField(default="")
    update_description = models.CharField(max_length=5000)
    timestamp = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.update_description[0:15] + "..."
