from django.shortcuts import render, redirect
from .models import Pet
from .forms import PetForm, NotAvailableForm


def pet_list (request):
	context = {
		"pets" : Pet.objects.all()
		}
	return render (request, 'list.html', context)

def pet_detail (request, pet_id):
	context = {
		"pets": Pet.objects.get (id = pet_id)
	}
	return render (request, 'detail.html', context)

def pet_create (request):
	form =  NotAvailableForm ()
	##WHAT IS THIS LINE DOING?
	if request.method == "POST":
		form = NotAvailableForm (request.POST)
		if form.is_valid ():
			form.save()
			return redirect ('pet-list')
	##WHAT HAPPENS IF THE BELOW CODE LINE IS NOT INCLUDED
	context = { 
		"form" : form,
		}
	return render (request, 'create.html', context)

def pet_update(request, pet_id):
	##IS PET PET_OBJ A NAME WE ASSIGNED
    pet_obj = Pet.objects.get(id=pet_id)
    form = PetForm(instance=pet_obj)
    if request.method == "POST":
        form = PetForm(request.POST, request.FILES, instance=pet_obj)
        if form.is_valid():
            form.save()
            return redirect('pet-detail')
    context = {
        "pet_obj": pet_obj,
        "form":form,
    }
    return render(request, 'update.html', context)

def pet_delete(request, pet_id):
    pet_obj = Pet.objects.get(id=pet_id)
    pet_obj.delete()
    return redirect('pet-list')
