from django.db import models
from enum import Enum

# Create your models here.
class ConditionChoice(Enum):
    BRAND_NEW = "Brand new"
    USED = "Used"
    LIKE_NEW = "Like new"

class StateChoice(Enum):
    AL = "Alabama"
    AK = "Alaska"
    AZ = "Arizona"
    AR = "Arkansas"
    CA = "California"
    CO = "Colorado"
    CT = "Connecticut"
    DE = "Delaware"
    FL = "Florida"
    GA = "Georgia"
    HI = "Hawaii"
    ID = "Idaho"
    IL = "Illinois"
    IN = "Indiana"
    IA = "Iowa"
    KS = "Kansas"
    KY = "Kentucky"
    LA = "Louisiana"
    ME = "Maine"
    MD = "Maryland"
    MT = "Montana"
    NE = "Nebraska"
    NV = "Nevada"
    NH = "New Hampshire"
    NJ = "New Jersey"
    NM = "New Mexico"
    NY = "New York"
    NC = "North Carolina"
    ND = "North Dakota"
    OH = "Ohio"
    OK = "Oklahoma"
    OR = "Oregon"
    PA = "Pennsylvania"
    RI = "Rhode Island"
    SC = "South Carolina"
    SD = "South Dakota"
    TN = "Tennessee"
    TX = "Texas"
    UT = "Utah"
    VT = "Vermont"

class CategoryChoice(Enum):
    CLOTHES = "Clothes"
    SHOES = "Shoes"
    HANDBAGS = "Handbags"
    BABY_STUFF = "Baby stuff"
    HOUSEHOLD = "Household"
    ELECTRONICS = "Electronics"
    FURNITURE = "Funiture"
    MISC = "Miscellaneous"



class Product(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name=“product”)
    sellingStatus =models.ForeignKey(Selling, on_delete=models.CASCADE, related_name=“product”)
    product_name = models.CharField(max_length = 100)
    description = models.TextField()
    qty = models.PositiveSmallIntegerField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    image = models.ImageField(storage=fs)
    condition = models.CharField(max_length=10, choices=[(tag, tag.value) for tag in ConditionChoice])
    category = models.CharField(max_length=11, choices=[(tag, tag.value) for tag in CategoryChoice])


class Customer(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=15, choices=[(tag, tag.value) for tag in StateChoice])
    user_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    password = models.CharFileld(max_length=100)

class sellingStatus(models.Model):
    status = models.BooleanField()


class Message(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name=“message”)
    content = models.TextField()

