from django.db import models

# Create your models here.

class Item(models.Model):
    item_name = models.CharField(max_length= 100)
    item_desc = models.CharField(max_length= 100)
    price = models.IntegerField()
    item_image = models.URLField(default="https://endlessicons.com/wp-content/uploads/2012/11/loading-icon-614x460.png")
