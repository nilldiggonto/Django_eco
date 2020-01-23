from django.db import models
from billing.models import BillingProfile
# Create your models here.

ADDRESS_TYPE = [
    ('billing','Billing'),
    ('shipping','Shipping'),
]


class Address(models.Model):
    billing_profile = models.ForeignKey(BillingProfile, on_delete='DO_NOTHING')
    address_type    = models.CharField(max_length=120, choices = ADDRESS_TYPE)
    address_line_1  = models.CharField(max_length=120)
    address_line_2  = models.CharField(max_length=120)
    country         = models.CharField(max_length=120, default='BD')
    city            = models.CharField(max_length=120)
    state           = models.CharField(max_length=120)
    postal_code     = models.CharField(max_length=120)

    def __str__(self):
        return str(self.billing_profile)
    def get_address(self):
        line1 = self.address_line_1
        line2 = self.address_line_2
        city = self.city
        state = self.state
        city = self.city
        country = self.country
        return f"{line1}\n {line2} \n {city} \n ,{state}{city} \n {country}"
    