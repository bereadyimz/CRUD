from django.shortcuts import render
from .forms import EmployeeForm
from .models import Employee
from django.shortcuts import redirect

# Create your views here.
def Home(request):
    form=EmployeeForm()
    if request.method=='POST':
        form=EmployeeForm(request.POST)
        form.save()
        form=EmployeeForm()
         
    data = Employee.objects.all()     
    context={
        'form':form,
        'data':data,
    }
    return render(request, 'index.html', context) 



# Delete views...
def Delete_record(request, id):
    a= Employee.objects.get(pk=id)
    a.delete()
    return redirect('/')


# Update_record...
def update_record(request, id):
    if request.method=='POST':
        data=Employee.objects.get(pk=id)
        form=EmployeeForm(request.POST,instance=data)
        if form.is_valid():
            form.save()
    else:
        data= Employee.objects.get(pk=id)
        form=EmployeeForm(instance=data)
    context={
        'form':form,
    }
    return render(request,'update.html',context)