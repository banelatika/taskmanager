from django.db import models
from django.contrib.auth.models import User, Group

# Create your models here.

class profile(models.Model):
   
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    is_active = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)
    gruop = models.ForeignKey(Group, on_delete=models.CASCADE)

class TaskUser(models.Model):
    checkbox = models.BooleanField(default=False)
    taskdetails = models.TextField()
    assignee = models.ForeignKey(User, related_name="assignee",  on_delete=models.CASCADE)
    assignor = models.ForeignKey(User, related_name="assignor",  on_delete=models.CASCADE)



