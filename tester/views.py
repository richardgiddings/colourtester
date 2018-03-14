from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse

from .models import ColourCombo
from .forms import ColourComboForm

def index(request):
    colour_combos = ColourCombo.objects.all()

    return render(request, template_name='tester/index.html',
                  context={'combos': colour_combos})

def add_combo(request):
    if request.method == "POST":
        form = ColourComboForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('index'))
    else:
        form = ColourComboForm()

    return render(request, template_name='tester/combo.html',
                  context={'form': form})

def edit_combo(request, combo_id):
    combo = ColourCombo.objects.get(id=combo_id)
    if request.method == "POST":
        form = ColourComboForm(request.POST, instance=combo)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('index'))
    else:
        form = ColourComboForm(instance=combo)

    return render(request, template_name='tester/combo.html',
                  context={'form': form})