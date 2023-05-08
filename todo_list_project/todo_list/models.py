from django.db import models

class TodoTask(models.Model):  
    title = models.CharField(max_length=100)  
    description = models.TextField(max_length=400) 
    duedate = models.DateField()
    complete = models.BooleanField(default=False)
    createuser =  models.CharField(max_length=100) 
  
    class Meta:  
        db_table = "todotask"