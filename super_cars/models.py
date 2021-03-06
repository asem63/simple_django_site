# coding: utf-8
from django.db import models


class Manufacturer(models.Model):
    name = models.CharField(max_length=200)

    def __unicode__(self):
        return u'%s' % (self.name)


class Car(models.Model):
    manufacturer = models.ForeignKey(Manufacturer)
    name = models.CharField(max_length=200)

    def __unicode__(self):
        return u'%s' % (self.name)
