from django.contrib import admin
from .models import Employee,Aadhar,Person,Department,Base2,Child2,Base3,Child3

# Register your models here.
admin.site.site_header='Amazon'

class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('empno','empname','salary','department','salaryGrade')
    list_filter = ('empno','salary')
    def salaryGrade(self,obj):
        if obj.salary>150000:
            return 'High'
        elif obj.salary>130000:
            return 'Medium'
        else:
            return 'Low'
        
class BaseAdmin(admin.ModelAdmin):
    list_display = ['empno','empname','salary']
    
    def __str__(self):
        return self.empname
        
        
admin.site.register(Employee,EmployeeAdmin)
admin.site.register(Aadhar)
admin.site.register(Person)
admin.site.register(Department)
admin.site.register(Base2)
admin.site.register(Child2)
admin.site.register(Base3,BaseAdmin)
admin.site.register(Child3,BaseAdmin)