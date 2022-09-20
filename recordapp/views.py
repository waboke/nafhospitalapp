from django.shortcuts import redirect, render, get_list_or_404, get_object_or_404
from django.http import HttpResponse, JsonResponse, HttpResponseRedirect
from django.contrib import messages
from django.urls import reverse
from .models import Patient_info
from .forms import Patient_info_form
#from open_folderapp.forms import FolderForm
#from addressapp.models import Address
from django.contrib.auth.decorators import login_required


# Create your views here.
@login_required
def record_home(request):
    patient_form = Patient_info_form()
    context ={'patient_form':patient_form}
    return render(request, 'recordapp/home1.html', context)

@login_required   
def view_all_patients(request):
    all_patient= Patient_info.objects.all()
    context = {'all_patient' : all_patient}
    return render(request, 'recordapp/view-all-patients1.html', context )
@login_required
def add_patient(request): 
    if request.method =="POST":
        patient_form = Patient_info_form(request.POST)
        if patient_form.is_valid():
            patientid=patient_form.save()
            patient_details = patientid.id
            messages.success(request, "Patient Details added  successfully." )
            return redirect('recordapp:add-address', pk=patient_details)
        else:
            messages.error(request, "Patient hospital No or email address already exist")
            context ={'patient_form':patient_form}
            return render(request, 'recordapp/add-new-patients1.html', context)

    else: 
        patient_form = Patient_info_form()    
        context ={'patient_form':patient_form}
        return render(request, 'recordapp/add-new-patients1.html', context)
@login_required
def update_details(request, id):
    try:
        get_user_data = get_object_or_404(Patient_info, pk=id)
        patient_form = Patient_info_form(instance=get_user_data)
        if request.method == 'POST':
            form = Patient_info_form(request.POST, instance=get_user_data)
            if form.is_valid():
                patientid=form.save()
                patient_details = patientid.id
                messages.success(request, 'patient details updated')
            return redirect('recordapp:patient-details', pk=patient_details)
    except Patient_info.DoesNotExist:
        raise Http404("Patient details with " + get_user_data +" does not exist")

    context = { 'patient_form':patient_form }
    return render(request, 'recordapp/update-details.html', context)

@login_required      
def patient_details(request, pk):
    patient_details = Patient_info.objects.get(id=pk)
    # address = Address.objects.get(id=pk)
    form = FolderForm(request.POST or None)
    try:
        address = Address.objects.get(patient_info=pk)
        context = {'patient_details' : patient_details, 
        'form': form, 'address':address}
        template_name = 'recordapp/patientProfile.html'
        return render(request, template_name, context)
    except Address.DoesNotExist:
        context = {'patient_details' : patient_details,'form': form}
        template_name = 'recordapp/patientProfile.html'
        return render(request, template_name, context)

    
@login_required
def delete_details(request, id):
    get_user = get_object_or_404(Patient_info, pk=id)
    if request.method == 'POST':
        get_user.delete()
        messages.error(request, 'User deleted')
        return redirect('recordapp:all-patients')
    return render(request, 'recordapp/delete-patient.html', {})
    
def success(request):
    return render(request, 'recordapp/success.html', { })
# new patient end
