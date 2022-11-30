from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *
from .forms import ContactForm
from .models import Contact
from django.db.models import Q

# Create your views here.
def homepage(request):
  if request.method == "POST":
    form = ContactForm(request.POST)
    if form.is_valid():
      form.save()
  contacts = Contact.objects.all().order_by('name', 'profession').values()
  form = ContactForm()
  return render(request, "home.html", {"form": form, "contacts":contacts})


def updateContact(request,pk):

	contact= Contact.objects.get(id=pk)
	form= ContactForm(instance=contact)
	
	if request.method =="POST":
		#print("printing POST:", request.POST)
		form= ContactForm(request.POST, instance=contact)
		if form.is_valid():
			form.save()
			return redirect('/')
	context ={'form':form}
	return render(request, 'home.html',context)


def deleteContact(request,pk):
	contact= Contact.objects.get(id=pk)
	if request.method=='POST':
		contact.delete()
		return(redirect('/'))
	context ={'contact':contact}
	return render(request, "delete_contact.html", context)

def searchName(request):
  if request.method == "POST":
    searched = request.POST.get('searched')
    contacts= Contact.objects.filter(Q(name__contains=searched) | Q(mobile_number__contains=searched))
    return render(request, "search_name.html", {'searched':searched, 'contacts':contacts})
  else:
    return render(request, "search_name.html", {})

def searchProfession(request):
  if request.method == "POST":
    searched = request.POST.get('searched')
    contacts= Contact.objects.filter(profession__contains=searched)
    return render(request, "search_profession.html", {'searched':searched, 'contacts':contacts})
  else:
    return render(request, "search_profession.html", {})

def compareName(request):
  if request.method == "POST":
    compared = request.POST.get('compared')
    compared2 = request.POST.get('compared2')

    contacts= Contact.objects.filter(name__contains=compared)
    contacts2= Contact.objects.filter(name__contains=compared2)
    
    return render(request, "compare_name.html", {'compared':compared, 'contacts':contacts, 'contacts2':contacts2, 'compared2':compared2})
  else:
    return render(request, "compare_name.html", {})
