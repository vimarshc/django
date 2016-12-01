from __future__ import unicode_literals

import datetime
from unittest import skipIf

from django.test import TestCase
from django.utils import six
from django.db.models import Prefetch

from .models import A,B,C,D

class Prefetch_Test_Case(TestCase):

    def test_case_for_only_nested_prefetches(self):
        a = A.objects.create()
        b = B.objects.create(a=a)
        d = D.objects.create()
        C.objects.create(b=b, d=d)

        queryset = A.objects.all().prefetch_related(
            Prefetch(
                'b',
                queryset=B.objects.all().prefetch_related(
                    Prefetch(
                        'c',
                        queryset=C.objects.all().prefetch_related(
                            'd'
                        )
                    )
                )
            )
        )
        content = queryset[0].b.c.all()[0].d.pk


        self.assertEqual(content, 1)


    def test_case_for_nested_and_flat_prefetches(self):
        a = A.objects.create()
        b = B.objects.create(a=a)
        d = D.objects.create()
        C.objects.create(b=b, d=d)

        queryset = A.objects.all().prefetch_related(
            Prefetch(
                'b',
                queryset=B.objects.all().prefetch_related(
                    Prefetch('c__d')
                )
            )
        )
        content = queryset[0].b.c.all()[0].d.pk

        self.assertEqual(content, 1)


    def test_case_for_only_flat_prefetches(self):
        a = A.objects.create()
        b = B.objects.create(a=a)
        d = D.objects.create()
        C.objects.create(b=b, d=d)

        queryset = A.objects.all().prefetch_related(
            Prefetch('b__c__d')
        )
        content = queryset[0].b.c.all()[0].d.pk

        self.assertEqual(content, 1)
