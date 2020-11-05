from django.shortcuts import render
from.models import Sendemail
from django.core.mail import send_mail
from.forms import SendemailForm
from django.conf import settings
# Create your views here.
def send_email(request):
	obj=Sendemail.objects.first()
	if request.method=='POST':
		subject=request.POST['subject']
		email=request.POST['email']
		message=request.POST['message']
		send_mail(
		    subject,
		    message,
		    settings.EMAIL_HOST_USER,
		    [email],
		    fail_silently=False,
		    
		)
		
	
	return render(request,'send_form.html',{'obj':obj})

