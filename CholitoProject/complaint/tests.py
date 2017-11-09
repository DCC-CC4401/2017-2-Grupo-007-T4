from django.test import TestCase
from complaint.models import Complaint

class ComplaintTestCase(TestCase):
    def setUp(self):
        Complaint.objects.create(descripction="Perro herido en la carretera", case ='1', lat=-33, lng= -70, directions= "Plaza de armas SN  Casilla 52D")

    def test_not_null(self):
        """Animals that can speak are correctly identified"""
        perrito = Complaint.objects.get(name="Santiago")
        self.assertTrue(perrito!=None)