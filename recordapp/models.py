from django.db import models
from django.urls import reverse
from django.utils.text import slugify
from datetime import datetime, date
import datetime
from uuid import uuid4



# Create your models here.
class Personal_info(models.Model):
    Gender_Choices = [
        ('M', 'Male'),
        ('F', 'Female'),
           ]
        
    
    fname = models.CharField(max_length=120, blank=True, null=True)
    mname = models.CharField(max_length=120, blank=True, null=True)
    lname = models.CharField(max_length=120, blank=True, null=True)
    data_of_birth = models.DateField(blank=True, null=True)
    sex = models.CharField(max_length=1, blank=True, null=False)
    email = models.CharField(max_length=120, blank=True, null=True, unique= True)
    created_on = models.DateTimeField(auto_now=False, auto_now_add=True, blank=True, null=True)
    updated_on = models.DateTimeField(auto_now=True, auto_now_add=False, blank=True, null=True)
    phone_number = models.CharField(max_length=120, blank=True, null=True)
    class Meta:
        abstract = True
def create_no():
        now = datetime.datetime.now()
        return str(now.year)+str(now.month)+str(now.day)+str(uuid4())[:7]

class Patient_info(Personal_info):
   
    hospitalNo = models.CharField(max_length=120, blank=True, null=True, unique=True )
    occupation = models.CharField(max_length=120, blank=True, null=True)
    state_of_origin = models.CharField(max_length=120, blank=True, null=True)
    city = models.CharField(max_length=120, blank=True, null=True)
    tribe = models.CharField(max_length=120, blank=True, null=True)
    religion = models.CharField(max_length=1, blank=True, null=True)
    status = models.CharField(max_length=10, blank=True, null=False)
    patient_type = models.CharField(max_length=10, blank=True, null=False)
    slug = models.SlugField(blank=True, default='') # < here
    def __self__(self):
        return self.fname
    
    def save(self, *args, **kwargs): # < here
        self.slug = slugify(self.hospitalNo)
        super(Patient_info, self).save()
    
    def get_absolute_url_update(self):
        return reverse('recordapp:update-patient', args=[str(self.id)])
   
    @property
    def full_names(self):
        return '%s %s' % (self.fname, self.lname)
    @property
    def age(self):
        age = 0;
        if(age != None):
            age = int((datetime.now().date() - self.data_of_birth).days / 365.25)
            return age
    @property
    def age1(data_of_birth):
        today = date.today()
        age = today.year - data_of_birth.year - ((today.month, today.day) < (data_of_birth.month, data_of_birth.day))
        return 
    property
    def get_age(self):
        age = datetime.date.today()-self.data_of_birth
        return int((age).days/365.25)
    
    def save(self, *args, **kwargs):
        today = datetime.datetime.now()
        # year = today.year
        # year_sring= str(year)
        today_string = today.strftime('%y%m%d')
        next_hospital_number = '01'
        last_hospital_number = Patient_info.objects.filter(hospitalNo__startswith=today_string).order_by('hospitalNo').last()
        if last_hospital_number:
            last_hospital_number = int(last_hospital_number.hospitalNo[6:])
            next_hospital_number = '{0:02d}'.format(last_hospital_number + 1)
        self.hospitalNo = today_string + next_hospital_number
        super(Patient_info, self).save(*args, **kwargs)
    
class patient_pic(models.Model):
    personal_info = models.OneToOneField(Patient_info, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='patients_pic', default='default.jpg')
    updated_on = models.DateTimeField(auto_now=True, auto_now_add=False, blank=True, null=True)
    class Meta:
        verbose_name_plural ="patient_pic"
    