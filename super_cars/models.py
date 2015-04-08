from django.db import models

# Create your models here.

class Manufacturer(models.Model):
    name = models.CharField(max_length=200)

    def __unicode__(self):
        return u'%s' % (self.name)

class Car(models.Model):
    manufacturer =  models.ForeignKey(Manufacturer)
    name = models.CharField(max_length=200)
    
    def __unicode__(self):
        return u'%s' % (self.name)
