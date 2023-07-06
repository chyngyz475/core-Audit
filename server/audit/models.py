from django.db import models

class Dict(models.Model):
    class Meta:
        db_table='dict'
        managed=False
        
    code = models.CharField(max_length=25, null=True)
    name=models.CharField(max_length=500, null=True)

class Dict_type(models.Model):
    class Meta:
        db_table='dict_type'
        managed=False

    name = models.CharField(max_length=100, null=True)