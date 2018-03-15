from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib import messages

from .models import ColourCombo
from .forms import ColourComboForm
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

def index(request):
    colour_combos = ColourCombo.objects.all().order_by('-created_at')

    paginator = Paginator(colour_combos, 5) # Show n results per page
    page = request.GET.get('page')
    try:
        colour_combos = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        colour_combos = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        colour_combos = paginator.page(paginator.num_pages)

    return render(request, template_name='tester/index.html',
                  context={'combos': colour_combos})

def add_combo(request):
    if request.method == "POST":
        form = ColourComboForm(request.POST)
        if form.is_valid():
            if request.POST.get("save-button"):
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
            if request.POST.get("save-button"):
                form.save()
                return HttpResponseRedirect(reverse('index'))
    else:
        form = ColourComboForm(instance=combo)
        

    return render(request, template_name='tester/combo.html',
                  context={'form': form})