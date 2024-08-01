from django.db import models


class Todo_Task(models.Model):
    Status = [('In Progress', 'In Progress'), ('Complated', 'Complated'), ('Pending', 'Pending')]
    task_name = models.CharField(max_length=50)
    task_description = models.TextField()
    task_status = models.CharField(max_length=15, choices=Status, default='Pending')
    task_deadline = models.DateField()
    task_created_date = models.DateField(auto_now_add=True)
    task_completed = models.DateField(blank=True, null=True)

