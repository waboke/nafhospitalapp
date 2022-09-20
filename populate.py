import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mysite.settings')
import django
django.setup()

# FAKE POP SCRIPT
import random
import numpy as np
from recordapp.models import Patient_info, patient_pic, Rank, Unit, Next_of_kin, Address
from faker import Faker

fakegen = Faker()
def populate(N=5):
    sex =['M', 'F']
    services =['Army', 'Navy', 'Airforce', 'Police', 'Imigration']
    rank =['LCp', 'ACM', 'Cp', 'Sgt', 'WO']
    relation =['brother', 'sister', 'child', 'spouse']
    tribes = ['ibo', 'Hausa', 'Yoruba']
    religion =['Christianity', 'Islam','Others']
    PATIENT_STATUS = ['NHIS','Not NHIS']
    PATIENT_TYPE = ['CIV','Pesonnel']

    for _ in range(N):
        fake_fname = fakegen.first_name()
        fake_mname = fakegen.last_name()
        fake_lname = fakegen.last_name()
        fake_date = fakegen.date_of_birth()
        fake_sex = np.random.choice(sex)
        fake_email = fakegen.email()
        fake_timestamp = fakegen.date_time()
        fake_image = fakegen.image( image_format='jpeg')
        fake_service = fakegen.name()
        fake_rank_name =fakegen.name()
        fake_name = fakegen.name()
        fake_services = np.random.choice(services)
        fake_rank = np.random.choice(rank)
        fake_fullname =fakegen.name()
        fake_address = fakegen.address()
        fake_relation = np.random.choice(relation)
        fake_phone = fakegen.phone_number()
        fake_street_no = fakegen.building_number()
        fake_state = fakegen.state()
        fake_lga = fakegen.administrative_unit()
        fake_city = fakegen.city()
        fake_street_name = fakegen.street_name()
        fake_hospital_no = fakegen.random.randint(1, 9999)
        fake_occupation = fakegen.job()
        fake_tribe = np.random.choice(tribes)
        fake_religion = np.random.choice(religion)
        fake_status = np.random.choice(PATIENT_STATUS)
        fake_type = np.random.choice(PATIENT_TYPE)
        
        Patient = Patient_info.objects.get_or_create(
            fname= fake_fname, 
            mname=fake_mname,
            lname=fake_lname,
            data_of_birth=fake_date,
            sex=fake_sex,
            email=fake_email,
            phone_number=fake_phone,
            hospitalNo =fake_hospital_no,
            occupation = fake_occupation,
            state_of_origin = fake_state,
            city = fake_city,
            tribe= fake_tribe,
            religion= fake_religion,
            status= fake_status,
            patient_type= fake_type,
            )[0]
        
        # rank = Rank.objects.get_or_create(
        # personal_info= Patient, 
        # name_of_service=fake_services,
        # rank_name=fake_rank)
        
        # next_of_kin = Next_of_kin.objects.get_or_create(
        # personal_info= Patient, 
        # fullName = fake_fullname,
        # address =fake_address,
        # relationship = fake_relation,
        # phone_number = fake_phone
        # )
        # address = Address.objects.get_or_create(
        # personal_info= Patient, 
        # street_no =fake_street_no,
        # street_name =fake_street_name,
        # state = fake_state,
        # lga = fake_lga,
        # city = fake_city
        
        # )
        # unit = Unit.objects.get_or_create(
        # personal_info= Patient, 
        # )
        
         
if __name__ =='__main__':
    print("populating")
    populate(20)
    print("end populating")
    