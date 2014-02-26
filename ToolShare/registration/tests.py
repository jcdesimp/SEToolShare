"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""

from django.test import TestCase
from django.test.utils import setup_test_environment
from django.core.urlresolvers import reverse
from shareCenter.models import UserProfile
from django.contrib.auth.models import User
from registration.models import RegistrationForm
from registration.views import register
from django import forms

        
def createUser(username, password, email, first_name, last_name):
    return User.objects.create(username=username, password=password, email=email,
                               first_name=first_name, last_name=last_name)
    
class testUserRegistration(TestCase):
    def test_index(self):
        resp = self.client.get('/registration/')
        self.assertEqual(resp.status_code, 200)
        
    def test_empty_fields(self):
        resp = self.client.get('/registration/')
        self.assertEqual(resp.status_code, 200)
        resp = self.client.post("/registration/", {'username': ''})
        self.assertFormError(resp, 'form', 'username', 'This field is required.')
        resp = self.client.post("/registration/", {'password': ''})
        self.assertFormError(resp, 'form', 'password', 'This field is required.')
        resp = self.client.post("/registration/", {'email': ''})
        self.assertFormError(resp, 'form', 'email', 'This field is required.')
        resp = self.client.post("/registration/", {'firstName': ''})
        self.assertFormError(resp, 'form', 'firstName', 'This field is required.')
        resp = self.client.post("/registration/", {'lastName': ''})
        self.assertFormError(resp, 'form', 'lastName', 'This field is required.')
        
  
        
    
        
        
        
        
        
        