from django.test import TestCase
from django.contrib.auth.models import User
from .models import Task
from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
from rest_framework_simplejwt.tokens import RefreshToken

# Create your tests here.
class TaskManagerAPI(APITestCase):
    def setUp(self):
        self.user=User.objects.create_user(username="testuser", password="testpass")
        response=self.client.post(reverse("login"), {"username":"testuser", "password":"testpass"})
        self.token=response.data['access']
        self.client.credentials(HTTP_AUTHORIZATION=f"Bearer {self.token}")
        self.task = Task.objects.create(
            title="Existing Task",
            description="This is an existing task",
            due_date="2025-09-30",
            priority=1,
            status="pending",
            user=self.user
        )
    
    def test_create_task(self):
        url=reverse("task-list")
        data={
            "title":"New Task",
            "description":"This is a new task",
            "due_date":"2023-11-30",
            "priority":2,
            "status":"in-progress"
        }
        response=self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Task.objects.count(), 2)
        self.assertEqual(Task.objects.get(id=response.data['id']).title, "New Task")
    
    def test_get_tasks(self):
        url=reverse("task-list")
        response=self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
    
    def test_update_task(self):
        url=reverse("task-detail", args=[self.task.id])
        data={
            "title":"Updated Task",
            "description":"This task has been updated",
            "due_date":"2025-09-14",
            "priority":3,
            "status":"completed"
        }
        response=self.client.put(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.task.refresh_from_db()
        self.assertEqual(self.task.title, "Updated Task")
        self.assertEqual(self.task.status, "completed")
    
    def test_delete_task(self):
        url=reverse("task-detail", args=[self.task.id])
        response=self.client.delete(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Task.objects.count(), 0)
