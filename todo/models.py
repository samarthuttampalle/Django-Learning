from django.db import models

class Task(models.Model):
    task = models.CharField(max_length=250)
    is_completed = models.BooleanField(default=False)
    createdd_at = models.DateTimeField(auto_now_add=True)
    upadetd_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.task
