# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.test import TestCase
from .models import A,B,C,D


class Flattened_Prefetch(TestCase):

    def test_basic(self):
        a = A.objects.create()
        b = B.objects.create()

        b.a = a
        b.save()

        d = D.objects.create()
        C.objects.create(b=b, d=d)

        if a and b and d:
            content = 1
        else:
            content = 9

        self.assertEqual(1,content)
