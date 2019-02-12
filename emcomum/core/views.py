from django.core import mail
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render
from django.template.loader import render_to_string
from emcomum.core.forms import IntroduceForm

def home(request):
    if request.method == 'POST':
        form = IntroduceForm(request.POST)
        if form.is_valid():
            body = render_to_string('email.html', form.cleaned_data)

            mail.send_mail('Em comum',
                       body,
                       'em@comum.org',
                       [form.cleaned_data['person1_email'], form.cleaned_data['person2_email']])

            return HttpResponseRedirect('/obrigado')
        else:
            return render(request, 'index.html', {'form': form})

    else:
        context = {'form': IntroduceForm()}
        return render(request, 'index.html', context)
