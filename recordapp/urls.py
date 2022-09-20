from django.urls import path, include
from . import views
app_name = 'recordapp'
urlpatterns = [
    path('record-home', views.record_home, name='home'),
    path('all-patients', views.view_all_patients, name='all-patients'),
    path('update-patient/<int:id>/', views.update_details, name='update-patient'),
    path('patient-details/<int:pk>/', views.patient_details, name='patient-details'),
    path('delete/<int:id>', views.delete_details, name='delete'),
    path('new-patient-form/', views.add_patient, name='add-new-patient'),
]
