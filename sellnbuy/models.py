from django.db import models
# from enum import Enum
from django.contrib.auth.models import User
from django.utils.translation import gettext as _
from model_utils import Choices

from django.db.models.signals import post_save
from django.dispatch import receiver


# class State(models.Model):
#     state = models.CharField(max_length=20)

#     def __str__(self):
#         return self.state

# class Profile(AbstractUser):
#     address = models.CharField(max_length=100)
#     city = models.CharField(max_length=100)
#     state = models.ForeignKey(State, on_delete=models.CASCADE, related_name="customer")
#     zipcode = models.CharField(max_length=10, blank = True)

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    address = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    # state = models.CharField(max_length=40)
    # state = models.ForeignKey(State, on_delete=models.CASCADE, related_name="customer")
    zipcode = models.CharField(max_length=10, blank = True)
    STATE = Choices(('AL', 'Alabama'), 
                    ('AK', 'Alaska'),
                    ('AZ', 'Arizona'), 
                    ('AR', 'Arkansas'), 
                    ('CA', 'California'),
                    ('CO', 'Colorado'), 
                    ('CT', 'Connecticut'),
                    ('DE', 'Delaware'),
                    ('DC', 'District of Columbia'), 
                    ('FL', 'Florida'), 
                    ('GA', 'Georgia'), 
                    ('HI', 'Hawaii'), 
                    ('ID', 'Idaho'), 
                    ('IL', 'Illinois'), 
                    ('IN', 'Indiana'), 
                    ('IA', 'Iowa'), 
                    ('KS', 'Kansas'), 
                    ('KY', 'Kentucky'), 
                    ('LA', 'Louisiana'), 
                    ('ME', 'Maine'), 
                    ('MD', 'Maryland'), 
                    ('MA', 'Massachusetts'), 
                    ('MI', 'Michigan'), 
                    ('MN', 'Minnesota'), 
                    ('MS', 'Mississippi'), 
                    ('MO', 'Missouri'), 
                    ('MT', 'Montana'), 
                    ('NE', 'Nebraska'), 
                    ('NV', 'Nevada'), 
                    ('NH', 'New Hampshire'), 
                    ('NJ', 'New Jersey'), 
                    ('NM', 'New Mexico'), 
                    ('NY', 'New York'), 
                    ('NC', 'North Carolina'), 
                    ('ND', 'North Dakota'), 
                    ('OH', 'Ohio'), 
                    ('OK', 'Oklahoma'), 
                    ('OR', 'Oregon'), 
                    ('PA', 'Pennsylvania'), 
                    ('RI', 'Rhode Island'), 
                    ('SC', 'South Carolina'), 
                    ('SD', 'South Dakota'), 
                    ('TN', 'Tennessee'), 
                    ('TX', 'Texas'), 
                    ('UT', 'Utah'), 
                    ('VT', 'Vermont'), 
                    ('VA', 'Virginia'), 
                    ('WA', 'Washington'), 
                    ('WV', 'West Virginia'), 
                    ('WI', 'Wisconsin'), 
                    ('WY', 'Wyoming'))
    state = models.CharField(choices=STATE, max_length=30)
    
   
    def __str__(self):
        return self.user.first_name

@receiver(post_save, sender=User)
def update_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
        instance.profile.save()

class Product(models.Model):
    # Profile
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
    STATUS = Choices(
        ('sold', _('Sold')),
        ('avaialable', _('Available'))
    )
    sellingStatus = models.CharField(choices=STATUS, max_length=10)
    

    def __str__(self):
        return self.product_name



class Message(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name="message")
    content = models.TextField()

    def __str__(self):
        return self.content

 
 
#  insert into sellnbuy_profile(id, address, city, zipcode, state, user_id)
#  VALUES(1, "1234 14th street", "Gaithersburg", "20889", "Maryland", 2);

