from django.db import models

# Create your models here.
class CustomerCardDetails(models.Model):
    class Meta:
        verbose_name_plural = "customer card details"
        db_table = "customercarddetails"

    def __str__(self):
        return str(self.id)

    card_number = models.CharField(max_length=20, default=None, null=True)
    expiry_month = models.CharField(max_length=2, default=None, null=True)
    expiry_year = models.CharField(max_length=2, default=None, null=True)
    cvv = models.CharField(max_length=3, default=None, null=True)
    is_active = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class States(models.Model):
    class Meta:
        verbose_name_plural = "state list"

    def __str__(self):
        return "{} {}".format(self.id, self.name)

    name = models.CharField(max_length=50, default=None, null=True)
    slug = models.CharField(max_length=50, default=None, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(auto_now=True)
    is_deleted = models.BooleanField(default=False)