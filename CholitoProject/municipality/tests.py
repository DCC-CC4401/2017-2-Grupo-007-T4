
from django.test import TestCase
from municipality.models import Municipality

class MunicipalityTestCase(TestCase):
    def setUp(self):
        Municipality.objects.create(name="Santiago", lat=-33, lng= -70, directions= "Plaza de armas SN  Casilla 52D")

    def test_not_null(self):
        """Animals that can speak are correctly identified"""
        Santiago = Municipality.objects.get(name="Santiago")
        self.assertTrue(Santiago!=None)