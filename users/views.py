from django.shortcuts import redirect
from django.contrib import messages
from django.http import HttpResponse


def login_error(request):
    messages.add_message(request, messages.ERROR,
        'Please use the correct Google account (same email with a staff account).')

    return redirect('/admin')

def index(request):
    return HttpResponse('Only the administrative part of the site is available.')