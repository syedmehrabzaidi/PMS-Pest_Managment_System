from django.db import models

# Create your models here.
class table1(models.Model):
    pestname = models.CharField(max_length=60)
    pesttype = models.CharField(max_length=60)
    tl = models.CharField(max_length=60)
    tu = models.CharField(max_length=60)
    dd = models.CharField(max_length=60)

    
    def __str__(self):
        return self.pestname
    

class Pest_table(models.Model):
    name = models.CharField(max_length=60)
    pesttype = models.CharField(max_length=60)
    tl = models.CharField(max_length=60)
    tu = models.CharField(max_length=60)
    dd = models.CharField(max_length=60)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Pest_table"

#class Rice(models.Model):
 #   date = models.models.DateTimeField(auto_now_add=True)
 #   dd = models.CharField(max_length=60)
 #   tl = models.CharField(max_length=60)
 #   accumulate = models.CharField(max_length=60)
    