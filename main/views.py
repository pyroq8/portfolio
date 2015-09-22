from django.shortcuts import render, render_to_response
from django.template import RequestContext
from django.views.generic import View
from main.models import Skill, Timeline, Project, ProjectImage
from main.forms import SendEmail
from django.core.mail import send_mail
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponseRedirect
# Create your views here.


def home(request):

    context = {}

    context['projects'] = Project.objects.all()

    form = SendEmail()

    return render_to_response('index.html', context, context_instance=RequestContext(request))


@csrf_exempt
def send_email_view(request):

    if request.method == 'POST':
        form = SendEmail(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            phone_number = form.cleaned_data['phone_number']
            message = request.POST['message']

            fullemail = """%s, %s, %s:
%s""" % (name, email, phone_number, message)

            try:
                send_mail('Contact', fullemail, email, ['ALAWADHICOM@GMAIL.COM'])

                return HttpResponseRedirect('/')
            except:
              return HttpResponseRedirect('/')
        else:
          return HttpResponseRedirect('/')
    else:
        return HttpResponseRedirect('/')