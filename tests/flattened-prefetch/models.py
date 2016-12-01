from django.db import models


class A(models.Model):
    pass

class B(models.Model):
    a = models.ForeignKey(A)
    d = models.ManyToManyField('D', through='C', related_name='b')

class C(models.Model):
    b = models.ForeignKey('B', related_name='c')
    d = models.ForeignKey('D', related_name='c')


class D(models.Model):
    pass