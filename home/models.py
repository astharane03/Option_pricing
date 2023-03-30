from django.db import models

# Create your models here.


class OptionInfo(models.Model):
    type=models.CharField(max_length=30)
    rate=models.IntegerField()
    upfactor=models.IntegerField()
    downfactor=models.IntegerField()
    timeperiod=models.IntegerField()
    strikeprice=models.IntegerField(null=True)
    currentstockprice=models.IntegerField(null=True)


    

    