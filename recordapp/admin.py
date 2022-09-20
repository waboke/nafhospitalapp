from django.contrib import admin
from .models import Patient_info, patient_pic

# Register your models here.
class PatientAdmin(admin.ModelAdmin):
    list_display = ('id','hospitalNo', 'fname', 'mname','lname', 'data_of_birth', 'sex', 'email')
    
admin.site.register(Patient_info, PatientAdmin)
class PatientPic(admin.ModelAdmin):
    pass
admin.site.register(patient_pic, PatientPic)


