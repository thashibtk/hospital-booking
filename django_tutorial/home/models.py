from django.db import models

# Create your models here.
class Departments(models.Model):
    dept_name = models.CharField(max_length=100)
    dept_desc = models.TextField()
    
    def __str__(self):
        return self.dept_name 


class Doctors(models.Model):
    doct_name = models.CharField(max_length=200)
    doct_spec = models.CharField(max_length=300)
    dept_name = models.ForeignKey(Departments, on_delete=models.CASCADE)
    doct_img = models.ImageField(upload_to = 'doctors')