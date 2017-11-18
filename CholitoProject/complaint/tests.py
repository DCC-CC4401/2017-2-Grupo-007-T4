from django.test import TestCase
from complaint.models import Complaint,AnimalType
from municipality.models import Municipality, MunicipalityUser

class ComplaintTestCase(TestCase):
    def setUp(self):
        muni= Municipality.objects.create(name="Santiago", lat=-33, lng= -70, directions= "Plaza de armas SN  Casilla 52D")
        perro=AnimalType.objects.create(name="perro")
        Complaint.objects.create(description="Perro herido en la carretera", case ="1", lat=-33, lng= -70,
                                 directions= "Plaza de armas SN  Casilla 52D",status=1,animal_type=perro,
                                 gender="1", wounded="1", color="2", municipality =muni)

    def test_not_null(self):
        """Animals that can speak are correctly identified"""
        perrito = Complaint.objects.get(description="Perro herido en la carretera" )
        self.assertTrue(perrito!=None)