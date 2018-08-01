from django.db import models
from enum import Enum
# from django.core.files.storage import FileSystemStorage
from django.contrib.auth.models import User
from django.utils.translation import gettext as _
# from django.db.models.signals import post_save
# from django.dispatch import receiver
from model_utils import Choices
# fs = FileSystemStorage(location='/media/images')


# Create your models here.
# class ConditionChoice(Enum):
#     BRAND_NEW = "Brand new"
#     USED = "Used"
#     LIKE_NEW = "Like new" 

# class CategoryChoice(Enum):
#     CLOTHES = "Clothes"
#     SHOES = "Shoes"
#     HANDBAGS = "Handbags"
#     BABY_STUFF = "Baby stuff"
#     HOUSEHOLD = "Household"
#     ELECTRONICS = "Electronics"
#     FURNITURE = "Funiture"
#     MISC = "Miscellaneous"


# class SellingChoice(Enum):
#     SOLD = "Sold"
#     AVAILABLE = "Available"




class State(models.Model):
    state = models.CharField(max_length=20)

    def __str__(self):
        return self.state



class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    address = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    state = models.ForeignKey(State, on_delete=models.CASCADE, related_name="customer")
    zipcode = models.CharField(max_length=10, blank = True)
    
   
    def __str__(self):
        return self.user.first_name

# @receiver(post_save, sender=User)
# def create_user_profile(sender, instance, created, **kwargs):
#     if created:
#         Profile.objects.create(user=instance)

# @receiver(post_save, sender=User)
# def save_user_profile(sender, instance, **kwargs):
#     instance.profile.save()


class Product(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name="product")
    product_name = models.CharField(max_length = 100)
    description = models.TextField()
    qty = models.PositiveSmallIntegerField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    image = models.ImageField()
    CONDITION = Choices(('Brand new', _('Brand new')), ('Used', _('Used')), ('Like new', _('Like new')))
    # condition = models.CharField(max_length=10, choices=[(tag, tag.value) for tag in ConditionChoice])
    condition = models.CharField(choices=CONDITION, default=CONDITION['Brand new'], max_length=10)
    CATEGORY = Choices(
        ('clothes', _('Clothes')),
        ('shoes', _('Shoes')),
        ('handbags', _('Handbags')),
        ('baby_stuff', _('Baby Stuff')),
        ('household', _('Household')),
        ('electronics', _('Electronics')),
        ('furniture', _('Furniture')),
        ('misc', _('Miscellaneous'))
        )
    category = models.CharField(choices=CATEGORY, max_length=11)
    # category = models.CharField(max_length=11, choices=[(tag, tag.value) for tag in CategoryChoice])
    STATUS = Choices(
        ('sold', _('Sold')),
        ('avaialable', _('Available'))
    )
    sellingStatus = models.CharField(choices=STATUS, max_length=10)
    # sellingStatus =models.CharField(max_length=10, choices=[(tag, tag.value) for tag in SellingChoice])

    def __str__(self):
        return self.product_name



class Message(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name="message")
    content = models.TextField()

    def __str__(self):
        return self.content
