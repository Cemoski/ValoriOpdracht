"""""
In this file there are written several testcases for the app.

"""""
from rest_framework.reverse import reverse

from .models import Intern
from rest_framework.test import APITestCase
from rest_framework import status
from .serializers import InternSerializer


# Creating an intern
class createInternTestCase(APITestCase):

    def test_create_intern(self):
        data = {"first_name": "Omer", "last_name": "koprulu", "email": "koprulo001@hotmail.com", "phone_number":"0423412",
                "age":"44", "passed": "false"}
        response = self.client.post("/create-intern/", data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

#Deleting a specific intern testcase
class deleteInternTestCase(APITestCase):
    #Setting up data
    # def setUp(self):
         # Intern.objects.create(
         #    first_name='Omer',
         #    last_name='Koprulu',
         #    email='kopruluomer@live.nl Dog',
         #    phone_number='0648387761',
         #    age='28',
         #    passed='False')

    def test_delete_intern(self):
        # response = self.client.delete(reverse("delete-intern", kwargs={"pk": self.pk})) #Use the data which is setted up
        response = self.client.delete(reverse("delete-intern", kwargs={"pk": 10}))
        self.client.delete(response)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

#Calling internlist testcase
class showListInternTestCase(APITestCase):
    #Setting up data
    def setUp(self):
        Intern.objects.create(
            first_name='Omer',
            last_name='Koprulu',
            email='kopruluomer@live.nl Dog',
            phone_number='0648387761',
            age='28',
            passed='False')

        Intern.objects.create(
            first_name='Marco',
            last_name='Steen',
            email='kopruluomer@live.nl Dog',
            phone_number='0648387761',
            age='28',
            passed='False')

    def test_show_details_intern(self):
        # get API response
        response = self.client.get(reverse("intern-list"))
        # get data from db
        interns = Intern.objects.all()
        serializer = InternSerializer(interns, many=True)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
