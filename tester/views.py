from django.shortcuts import render
from .models import ColourCombo

def index(request):
    colour_combos = ColourCombo.objects.all()

    return render(request, template_name='tester/index.html',
                  context={'combos': colour_combos})

def combo(request):
    return render(request, template_name='tester/combo.html')