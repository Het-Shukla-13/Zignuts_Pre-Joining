from rest_framework.test import APITestCase
from .models import Product
from rest_framework import status
from django.urls import reverse
# Create your tests here.

class ProductAPITest(APITestCase):
    def setUp(self):
        self.product_url=reverse('product-list')
        self.product=Product.objects.create(
            name="Test Product",
            description="This is a test product",
            price=10.00,
            stock_quantity=100,
            category="Test Category"
        )

    def test_create_product(self):
        data={
            "name":"New Product",
            "description":"This is a new product",
            "price":20.00,
            "stock_quantity":50,
            "category":"New Category"
        }
        response=self.client.post(self.product_url,data,format='json')
        self.assertEqual(response.status_code,status.HTTP_201_CREATED)

    def test_get_product_list(self):
        response=self.client.get(self.product_url,format='json')
        self.assertEqual(response.status_code,status.HTTP_200_OK)
        self.assertGreaterEqual(len(response.data),1)

    def test_get_product_detail(self):
        url=reverse('product-detail',args=[self.product.id])
        response=self.client.get(url,format='json')
        self.assertEqual(response.status_code,status.HTTP_200_OK)
        self.assertEqual(response.data['name'],self.product.name)

    def test_update_product(self):
        url=reverse('product-detail',args=[self.product.id])
        data={
            "name":"Updated Product",
            "description":"This is an updated product",
            "price":15.00,
            "stock_quantity":80,
            "category":"Updated Category"
        }
        response=self.client.put(url,data,format='json')
        self.assertEqual(response.status_code,status.HTTP_200_OK)
        self.product.refresh_from_db()
        self.assertEqual(self.product.name,data['name'])

    def test_delete_product(self):
        url=reverse('product-detail',args=[self.product.id])
        response=self.client.delete(url,format='json')
        self.assertEqual(response.status_code,status.HTTP_204_NO_CONTENT)
        self.assertFalse(Product.objects.filter(id=self.product.id).exists())

    def test_create_product_invalid_price(self):
        data={
            "name":"Invalid Product",
            "description":"This product has invalid price",
            "price":-5.00,
            "stock_quantity":50,
            "category":"Invalid Category"
        }
        response=self.client.post(self.product_url,data,format='json')
        self.assertEqual(response.status_code,status.HTTP_400_BAD_REQUEST)
        self.assertIn('price',response.data)