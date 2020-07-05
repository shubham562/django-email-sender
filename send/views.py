from django.shortcuts import render
from django.core.mail import send_mail
# Create your views here.

def index(request):
    from_email = request.POST.get('from')
    to_email = request.POST.get('to')
    subject_email = request.POST.get('subject')
    message_email = request.POST.get('message')


    context = {'success': False}
    if request.method =='POST':
        send_mail(subject_email,
                  message_email,
                  from_email,
                  [to_email],
                  fail_silently=False,
                  auth_user='shubhamop@hushmail.com',
                  auth_password='subh@inscriptio.in')
        context = {'success':True}
    return render(request, 'index.html', context)
