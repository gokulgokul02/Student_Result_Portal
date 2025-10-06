from django.db import models

# Create your models here.
class Users(models.Model):
    name=models.CharField(max_length=50)
    reg_no=models.IntegerField(max_length=50)
    department=models.CharField(max_length=50,null=True)
    year_of_Study=models.CharField(max_length=50,null=True)
    clg_name=models.CharField(max_length=50)
    university_name=models.CharField(max_length=50)
    dob=models.CharField(max_length=50)

    def __str__(self):
        return self.name
    

class Results(models.Model):
    Users=models.ForeignKey(Users,on_delete=models.CASCADE)
    result=models.FileField(upload_to='results')

class Notification(models.Model):
    Message=models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
