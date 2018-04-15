from django.shortcuts import render,redirect, get_object_or_404

from .models import Egg
from .forms import EggForm

# Create your views here.
def list_eggs(request):
    eggs = Egg.objects.all()
    return render(request, 'eggs.html', {'eggs':eggs})

def new_egg(request):
    form = EggForm(request.POST or None, request.FILES or None)

    if form.is_valid():
        form.save()
        return redirect(list_eggs)

    return render(request, 'form.html', {'form':form})

def update_egg(request,id):
    egg = get_object_or_404(Egg, pk=id)
    form = EggForm(request.POST or None, request.FILES or None, instance=egg)

    if form.is_valid():
        form.save()
        return redirect(list_eggs)

    return render(request, 'form.html', {'form':form})

def delete_egg(request,id):
    egg = get_object_or_404(Egg, pk=id)

    if request.method == 'POST':
        egg.delete()
        return redirect(list_eggs)

    return render(request, 'confirm.html', {'egg': egg})
