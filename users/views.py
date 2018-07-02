from django.shortcuts import redirect
from django.contrib import messages

def login_error(request):
    messages.add_message(request, messages.ERROR, 
    'Please use the correct Google account (same email with a staff account).')

    return redirect('/admin')
