from django.shortcuts import render
from emcomum.core.forms import IntroduceForm

def home(request):
    context = {'form': IntroduceForm()}
    return render(request, 'index.html', context)
