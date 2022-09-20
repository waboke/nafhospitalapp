from django import forms
from . models import Patient_info
from django.forms.widgets import NumberInput, Select, TextInput

class Patient_info_form(forms.ModelForm):
    # hospitalNo = forms.CharField(error_messages={'required': ' Hospital Number Cannot be Empty'}, 
    #                              widget=forms.TextInput(attrs={'class': 'form-control ', 'type':'text',
    #                             'placeholder': 'Hospital Number', 'aria-label':'Hospital No', 'aria-describedby' :'addon-wrapping','id':'inputHospitalNumber',
    #                              }),
    #                               required=True)
    fname = forms.CharField( widget=forms.TextInput(attrs={'class': 'form-control', 'type':'text',
                                'placeholder': 'First Name', 'name': 'inputFirstName', 'id':'inputFirstName'
                                 }),
                                  required=True)
    mname = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control',  'type':'text',
                                'placeholder': 'Middle Name', 'name':'inputMiddleName', 'id':'inputMiddleName',
                                 }),
                                 
                                  )
    lname = forms.CharField(
                                 widget=forms.TextInput(attrs={'class': 'form-control',  'type':'text',
                                'placeholder': 'Last Name', 'name':'inputLastName', 'id':'inputLastName',
                                 }),
                                 
                                  required=True)
   
    data_of_birth = forms.DateField(
                                    input_formats=['%d/%m/%Y %H:%M'],
                                    widget=forms.DateInput(attrs={'class': 'form-control datetimepicker-input','type':'text','data-target': '#reservationdate'}))
       
    
    email = forms.EmailField(help_text='A valid email address, please.',
                                 widget=forms.TextInput(attrs={'class': 'form-control', 
                                'placeholder': 'Email','type':'email', 'name':'inputEmail', 'id':'inputEmail'
                                 }),
                                  required=False)
    phone_number = forms.CharField(
                                help_text='A valid phone number, please.',
                                label="phone number",
                                 widget=forms.TextInput(attrs={'class': 'form-control', 
                                'placeholder': 'phone number', 'name':'inputPhone', 'id':'inputPhone', 'type':'text'
                               
                                 }),required=False)
    occupation = forms.CharField(label="Profession",
                                 widget=forms.TextInput(attrs={'class': 'form-control' , 
                                'placeholder': 'Profession', 'name':'inputOccupation', 'id':'inputOccupation', 'type':'text'
                                 }),
                                  required=False)
    state_of_origin = forms.CharField(label="state of origin",
                                 widget=forms.TextInput(attrs={'class': 'form-control', 
                                'placeholder': 'state of origin','id':'inputState', 'type':'text',
                                'aria-label':'State', 'aria-describedby':'addon-wrapping'
                                 }),
                                  required=False)
    city = forms.CharField(label="City",
                                 widget=forms.TextInput(attrs={'class': 'form-control', 
                                'placeholder': 'City','id':'inputCity', 'type':'text',
                                'aria-label':'City', 'aria-describedby':'addon-wrapping'
                                 }),
                                  required=False)
    tribe = forms.CharField(label="Tribe",
                                 widget=forms.TextInput(attrs={'class': 'form-control input--style-4', 
                                'placeholder': 'Tribe','id':'inputTribe', 'type':'text',
                                'aria-label':'Tribe', 'aria-describedby':'addon-wrapping',
                                 }),
                                 required=False )
    
    data_of_birth = forms.DateField(label="Date of Birth",
                                 widget=forms.DateInput(format=('%d/%m/%Y'), attrs={'class':'form-control', 'placeholder':'Select Date of Birth',  'id':'id_date'}),
                                 required=False )

    CHOICES = [('M','Male'),('F','Female')]
    sex = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect( attrs={ 'type':'radio','style': 'display: inline-block'}))
    PATIENT_STATUS = [
        ('DHML', 'DHML'),
        ('NHIS', 'NHIS'),
        ('Not NHIS', 'Not NHIS'),
        ]
    status = forms.ChoiceField(choices=PATIENT_STATUS,  widget=forms.RadioSelect(attrs={ 'type':'radio' ,'name':'status', 'id':'status'}))

    PATIENT_TYPE = [
        ('CIV', 'Civillian'),
        ('Pesonnel', 'Personnel'),
        ]
    patient_type = forms.ChoiceField(choices=PATIENT_TYPE, widget=forms.RadioSelect( attrs={ 'type':'radio', 'name':'patient_type', 'id':'patient_type'}))


    RELIGION = [
        ('C', 'Christianity'),
        ('M', 'Islam'),
        ('O', 'Others'),
        ]
    religion = forms.ChoiceField(choices=RELIGION, widget=forms.RadioSelect( attrs={'class':'', 'type':'radio', 'name':'religion' ,'id':'religion'}))

    class Meta:
        model = Patient_info
        fields =['fname' , 'mname' ,'lname', 'data_of_birth', 'sex', 'email', 'phone_number', 'occupation',
         'state_of_origin', 'city','tribe','religion','status', 'patient_type']
    
    # def __init__(self, *args, **kwargs):
    #     super(Patient_info_form,self).__init__(*args, **kwargs)
    #     self.fields['hospitalNo'].required = True

# class Patient_address_form(forms.ModelForm):
#     class Meta:
#         model = Address
#         fields =['street_no', 'street_name', 'state', 'lga', 'city']

# class Patient_nok_form(forms.ModelForm):
#     class Meta:
#         model = Next_of_kin
#         fields =['fullName', 'address', 'relationship', 'phone_number']
