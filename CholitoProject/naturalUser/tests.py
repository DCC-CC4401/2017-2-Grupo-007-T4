from django.test import TestCase
from django.test import Client
from PIL import Image
from django.contrib.auth.models import User
from django.core.files.uploadedfile import SimpleUploadedFile
class testRegisterandLogin(TestCase):

    def testRegisterPost(self):
        #size = (200, 200)
        #color = (255, 0, 0, 0)
        #img = Image.new("RGBA", size, color)
        self.user = User.objects.create_user(username='John', email='JohnSmith@gmail.com', password='John12321')
        self.user.save()
        client = Client()

       # response = client.post('/signup/', {
        #    'tipo': 'Persona',
         #   'nombre': 'John',
          #  'apellido': 'Smith',
           # 'password': 'JohnSmith123',
            #'username': 'John',
            #'email': 'JohnSmith@gmail.com',
        #})
        #self.assertRedirects(response, '/')

        response = client.post('/login/', {
            'email': 'JohnSmith@gmail.com',
            'password': 'John12321',
        })

        self.assertRedirects(response, '/index')
