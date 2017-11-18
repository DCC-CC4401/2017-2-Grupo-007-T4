from django.test import TestCase

# Create your tests here.
from django.test import TestCase
from animals.models import Animal
from complaint.models import AnimalType

class ComplaintTestCase(TestCase):
    def setUp(self):
        perro = AnimalType.objects.create(name="perro")
        Animal.objects.create(name="cholito", gender="1", description =" desparacitado y esterilizado",
                              animal_type =perro, estimated_age=5, color="2" )

    def test_not_null(self):
        """Animals that can speak are correctly identified"""
        cholito= Animal.objects.get(name= "cholito")
        self.assertTrue(cholito!=None)