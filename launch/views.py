from django.http import HttpResponseRedirect
from django.template.context import RequestContext
from django.shortcuts import render_to_response
from django.core.urlresolvers import reverse

from launch.forms import SignupForm


def signup(request, template='launch/signup_page.html'):
    if "POST" == request.method:
        signup_form = SignupForm(data=request.POST)
        if signup_form.is_valid():
            signup_form.save()
            return HttpResponseRedirect(reverse('launch_page_success'))
    else:
        signup_form = SignupForm()
    context = {
        'signup_form' : signup_form,
    }
    return render_to_response(template, context, context_instance=RequestContext(request))

def success(request, template='launch/signup_complete.html'):
    context = {}
    return render_to_response(template, context, context_instance=RequestContext(request))