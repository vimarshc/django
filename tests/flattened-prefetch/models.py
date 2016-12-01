from django.db import models

#  A <-> B <-- C --> D
#        \__________/


class A(models.Model):
    pass


class B(models.Model):
    a = models.OneToOneField('A', null=True, related_name='b', on_delete=models.SET_DEFAULT)
    d = models.ManyToManyField('D', through='C', related_name='b')


class C(models.Model):
    b = models.ForeignKey('B', related_name='c', on_delete=models.SET_DEFAULT)
    d = models.ForeignKey('D', related_name='c', blank=True,null=True, on_delete=models.SET_DEFAULT)


class D(models.Model):
    pass
