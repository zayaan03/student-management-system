from django.db import models

# Create your models here.
class Student(models.Model):
    student_id = models.CharField(max_length = 14, unique = True)
    name = models.CharField(max_length = 50)
    email = models.EmailField()
    department = models.CharField(max_length = 50)
    semester = models.IntegerField(max_length = 1)
    cgpa = models.FloatField(max_length = 4)
    
    def __str__(self):
        return self.name
