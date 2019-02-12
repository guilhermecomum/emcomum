from django.core.mail import EmailMultiAlternatives
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from emcomum.core.forms import IntroduceForm

def home(request):
    if request.method == 'POST':
        form = IntroduceForm(request.POST)
        if form.is_valid():

            subject = 'Em comum'
            from_email = 'em@comum.org'
            to = [form.cleaned_data['person1_email'], form.cleaned_data['person2_email']]

            html_content = render_to_string('email.html', form.cleaned_data)
            text_content = strip_tags(html_content)

            msg = EmailMultiAlternatives(subject, text_content, from_email, to)
            msg.attach_alternative(html_content, "text/html")
            msg.send()

            return HttpResponseRedirect('/obrigado')
        else:
            return render(request, 'index.html', {'form': form})

    else:
        context = {'form': IntroduceForm()}
        return render(request, 'index.html', context)
