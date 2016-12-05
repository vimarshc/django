from django.db import models



class A(models.Model):
    pass


class B(models.Model):
    a = models.OneToOneField('A', null=True, related_name='b', on_delete=models.CASCADE)
    d = models.ManyToManyField('D', through='C', related_name='b')


class C(models.Model):
    b = models.ForeignKey('B', related_name='c', on_delete=models.CASCADE)
    d = models.ForeignKey('D', related_name='c', on_delete=models.CASCADE)


class D(models.Model):
    pass
