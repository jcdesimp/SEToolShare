"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""
from django.test import TestCase
from django.test.utils import setup_test_environment
from django import forms
from shareCenter.models import ToolModel

class SimpleTest(TestCase):
    def test_basic_addition(self):
        """
        Tests that 1 + 1 always equals 2.
        """
        self.assertEqual(1 + 1, 2)
        
def createTool(owner, name, description, pickupInformation, location, available, timesUsed):
    return ToolModel.objects.create(owner=owner, name=name, description=description, pickupInformation=pickupInformation,
                                    location=location, available=available, timesUsed=0)
    
class TestToolModel(TestCase):
    def test_index(self):
        resp = self.client.get('/sharecenter/addtool')
        self.assertEqual(resp.status_code, 200)
        
    def test_empty_fields(self):
        resp = self.client.get('/sharecenter/addtool')
        self.assertEqual(resp.status_code, 200)
        resp = self.client.post("/sharecenter/addtool", {'name': ''})
        self.assertFormError(resp, 'form', 'name', 'This field is required.')
        resp = self.client.post("/sharecenter/addtool", {'description': ''})
        self.assertFormError(resp, 'form', 'description', 'This field is required.')
        resp = self.client.post("/sharecenter/addtool", {'pickupInformation': ''})
        self.assertFormError(resp, 'form', 'pickupInformation', 'This field is required.')
        
    def test_fields(self):
        resp = self.client.get('/sharecenter/addtool')
        self.assertEqual(resp.status_code, 200)
        resp = self.client.post("sharecenter/addtool", {'name': 'Hammer'})
        self.assertEqual(resp, 'form', 'name', 'Hammer')
        resp = self.client.post("sharecenter/addtool", {'description': 'Hammer things'})
        self.assertEqual(resp, 'form', 'description', 'Hammer things')
        resp = self.client.post("sharecenter/addtool", {'pickupInformation': 'My house'})
        self.assertEqual(resp, 'form', 'pickupInformation', 'My house')