from django.db import models
# Create your models here.
class Department(models.Model):
    Department = models.CharField(max_length=30,null=True)
    class Meta:
        verbose_name_plural = 'Departments'
    def __str__(self):
        return self.Department
 
class User(models.Model):
    Name = models.CharField(max_length=30,null=True,unique=True) 
    Email =  models.EmailField(max_length=50,null=True) 
    Phone_Number = models.CharField(max_length=50,null=True) 
    Password   =models.CharField(max_length=50,null=True) 
    Department_id=models.ForeignKey(Department,on_delete=models.CASCADE,null=True) 
    Role = models.CharField(max_length=30,null=True,unique=True)
    Created_by = models.BooleanField(default=True,null=True,blank=True)
    Created_at = models.BooleanField()
    Last_Updated_at = models.BooleanField()
    def __str__(self):
        return self.Name


class NewDepartment(models.Model):
    Name = models.CharField(max_length=30,null=True,unique=True)
    Description = models.TextField(max_length=250)
    Created_by= models.BooleanField(default=True,null=True,blank=True)
    Created_at=models.BooleanField()
    Last_Updated_at=models.BooleanField()
    def __str__(self): 
        return self.Name


class NewTickect(models.Model):
    Subject =  models.CharField(max_length=30,null=True,unique=True)
    Body = models.TextField()
    Priority = models.PositiveSmallIntegerField(("priority"),unique=True) 
    Email = models.EmailField(max_length=50,null=True) 
    Phone_Number= models.CharField(max_length=50,null=True) 
    class Meta:
        verbose_name_plural = 'NewTickects' 
        
    

    def __str__(self): 
        return self.Subject

class ManageTicket(models.Model):
    Ticket_ID =models.PositiveIntegerField(primary_key=True)
    Subject =models.ForeignKey(NewTickect,on_delete=models.CASCADE,null=True)  
    Priority = models.PositiveSmallIntegerField(("priority"),unique=True) 
    Created_at =models.BooleanField()         
    def __str__(self): 
        return self.Ticket_ID