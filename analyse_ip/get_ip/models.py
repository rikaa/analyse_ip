from django.db import models


class IPAddress(models.Model):
  pub_date = models.DateTimeField('date published')
  ip_address = models.IPAddressField()

