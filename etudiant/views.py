from django.http import HttpResponseRedirect
from django.shortcuts import render, HttpResponse
from .forms import StudentRegistration
from .models  import User 


# Create your views here.

def show(request):
    stud = User.objects.all()
    if request.method == 'POST':
     fm = StudentRegistration(request.POST)
     if fm.is_valid():
         nm = fm.cleaned_data['name']
         em = fm.cleaned_data['email']
         pw = fm.cleaned_data['password']
         reg = User(name = nm , email = em, password = pw)
         reg.save()
         fm = StudentRegistration()
    else:
      
       fm = StudentRegistration()

    return render(request, 'etudiant/afficher.html', {'form':fm, 'stu':stud })

def add_show(request):
    stud = User.objects.all()
    if request.method == 'POST':
     fm = StudentRegistration(request.POST)
     if fm.is_valid():
         nm = fm.cleaned_data['name']
         em = fm.cleaned_data['email']
         pw = fm.cleaned_data['password']
         reg = User(name = nm , email = em, password = pw)
         reg.save()
         fm = StudentRegistration()
    else:
      
       fm = StudentRegistration()

    return render(request, 'etudiant/addandshow.html', {'form':fm, 'stu':stud })

#update 

def update_data(request, id):
   
   if request.method == 'POST':
     pi = User.objects.get(pk=id)
     fm = StudentRegistration(request.POST, instance=pi)
     if fm.is_valid():
       fm.save()
   else:
    pi = User.objects.get(pk=id)
    fm = StudentRegistration(instance=pi)   

   return render(request, 'etudiant/updatestudent.html', {'form':fm})



#delete

def delete_data(request, id):
   if request.method == "POST":
      pi = User.objects.get(pk=id)
      pi.delete()
      return HttpResponseRedirect('/afficher'  )

