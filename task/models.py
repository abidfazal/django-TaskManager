from django.db import models
from django.utils import timezone
# Create your models here.

priority = (
    ('High','High'),
    ('Medium','Medium'),
    ('Low','Low'),
)

class Catagory(models.Model):
    name = models.CharField(max_length=200)
    
    
    def __str__(self) -> str:
        return self.name
    
class Task(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    catagory = models.ForeignKey(Catagory,on_delete=models.CASCADE)
    priority = models.CharField(max_length=10,choices=priority)
    date_of_creation = models.DateField(default=timezone.now)
    due_date  = models.DateField()

    is_completed = models.BooleanField(default=False)
    
    def __str__(self) -> str:
        return self.title
