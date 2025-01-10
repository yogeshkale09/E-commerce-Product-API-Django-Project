# Create your tests here.


from django.test import TestCase
from rest_framework.test import APITestCase
from rest_framework import status
from .models import Product

class ProductAPITestCase(APITestCase):
    def setUp(self):
        self.product = Product.objects.create(
            name="Test Product",
            description="A test product",
            price=100.00,
            stock=10,
            category="Test Category"
        )

    def test_create_product(self):
        data = {
            "name": "New Product",
            "description": "New description",
            "price": 50.00,
            "stock": 20,
            "category": "New Category"
        }
        response = self.client.post('/api/products/', data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_list_products(self):
        response = self.client.get('/api/products/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_update_product(self):
        data = {"price": 150.00}
        response = self.client.put(f'/api/products/{self.product.id}/', data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
