from django.db import models
from django.db.models.signals import pre_save,post_save,pre_delete,post_delete
from django.conf  import settings
from django.core.mail import send_mail
from django.dispatch import receiver

# Create your models here.

class Employee(models.Model):
    empno = models.IntegerField(primary_key=True)
    empname = models.CharField(max_length=20)
    salary = models.IntegerField()
    
def pre_save_handler(sender,instance,**kwargs):
    print("pre save handler has been called ")
    print(instance.empno,instance.empname,instance.salary)
pre_save.connect(pre_save_handler,sender=Employee)

def post_save_handler(sender,instance,created,**kwargs):
    print("Post save signal has been called")
    print(sender,created,instance.empno,instance.empname,instance.salary)
    subject = 'Alert on Employee'
    message = '''Below data is inserted into the table {},{},{}'''.format(instance.empno, instance.empname, instance.salary)
    from_user = settings.EMAIL_HOST_USER
    #to_user  = ['meenameenakshi224@gmail.com']
    #to_user = ['thirupathaiahjodu@gmail.com']
    #to_user = ['manjusri125@gmail.com']
    #to_user=['bukyakalyan70321@gmail.com']
    to_user = ['sivalayagna@gmail.com']
    send_mail(subject, message, from_user, to_user)
post_save.connect(post_save_handler,sender=Employee)

@receiver(pre_delete, sender=Employee)
def pre_delete_receiver(sender,instance,**kwargs):
    print("Pre save signal has been called")
pre_delete.connect(pre_delete_receiver, sender=Employee)
@receiver(post_delete, sender=Employee)

def post_delete_receiver(sender,instance,**kwargs):
    print("Post delete application is called")
    subject = 'Alert on Employee'
    message = '''Below data is deleted into the table {},{},{}'''.format(instance.empno, instance.empname, instance.salary)
    from_user = settings.EMAIL_HOST_USER
    to_user = ['pvnkumar.mekala@gmail.com']
    send_mail(subject,message,from_user,to_user)
post_delete.connect(post_delete_receiver, sender=Employee)

'''subject = 'welcome to GFG world'
message = f'Hi pavan, thank you for registering in geeksforgeeks.'
email_from = settings.EMAIL_HOST_USER
recipient_list = ['mekalapavankumar999@gmail.com', ]
send_mail(subject, message, email_from, recipient_list)'''
