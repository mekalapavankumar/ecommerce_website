from django.db import models

# Create your models here.


class Department(models.Model):
    deptno = models.IntegerField(primary_key=True)
    deptname = models.CharField(max_length=20)
    
    def __str__(self):
        return self.deptname

class Employee(models.Model):
    empno = models.IntegerField(primary_key=True)
    empname = models.CharField(max_length=20)
    salary = models.DecimalField(max_digits=10,decimal_places=2)
    department = models.ForeignKey(Department,null=True,on_delete=models.CASCADE)
    
    def __str__(self):
        return self.empname

class Aadhar(models.Model):
    aadhar_no = models.IntegerField(primary_key=True)
    
    def __str__(self):
        return str(self.aadhar_no)
    
class Person(models.Model):
    person_id = models.IntegerField(primary_key=True)
    person_name = models.CharField(max_length=20)
    
    aadhar = models.OneToOneField(Aadhar,on_delete=models.CASCADE)
    
    def __str__(self):
        return self.person_name
    
#abstract inheritance
class Base1(models.Model):
    empno = models.IntegerField(primary_key=True)
    empname = models.CharField(max_length=20)
    
    class Meta:
        abstract = True
        
class Child1(Base1):
    address = models.TextField()
    

#multiple inheritance
class Base2(models.Model):
    empno = models.IntegerField(primary_key=True)
    empname = models.CharField(max_length=20)
    
class Child2(Base2):
    address = models.TextField()

class Base3(models.Model):
    empno = models.IntegerField(primary_key=True)
    empname = models.CharField(max_length=20)
    salary = models.IntegerField()

class Child3(Base3):
    class Meta:
        proxy = True
        ordering = ['salary']

