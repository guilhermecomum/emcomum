from django.core.mail import EmailMultiAlternatives
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from emcomum.core.forms import MeetingForm
from emcomum.core.models import Meeting

def home(request):
    if request.method == 'POST':
        form = MeetingForm(request.POST)
        if form.is_valid():

            subject = 'Em Comum | {}, te enviou uma mensagem'.format(form.cleaned_data['host_name'])
            from_email = 'em@comum.org'
            to = [form.cleaned_data['host_email'], form.cleaned_data['guest1_email'], form.cleaned_data['guest2_email']]

            html_content = render_to_string('email.html', form.cleaned_data)
            text_content = strip_tags(html_content)

            msg = EmailMultiAlternatives(subject, text_content, from_email, to)
            msg.attach_alternative(html_content, "text/html")
            msg.send()

            Meeting.objects.create(**form.cleaned_data)

            return HttpResponseRedirect('/obrigado')
        else:
            return render(request, 'index.html', {'form': form})

    else:
        context = {'form': MeetingForm()}
        return render(request, 'index.html', context)

def thanks(request):
    return render(request, 'thanks.html')

def about(request):
    return render(request, 'about.html')
