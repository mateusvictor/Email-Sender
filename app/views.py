from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .models import Receiver
import os


@login_required
def home(request):	
	user = request.user
	receivers = [str(receiver) for receiver in Receiver.objects.filter(user=user)]

	context = {
		'receivers': ' | '.join(receivers),
	}
	
	return render(request, "app/home.html", context)


@login_required
def add_receiver(request):
	if request.method != 'POST':
		return redirect("home")

	user = request.user
	receiver = request.POST['receiver']
	new_receiver = Receiver.objects.create(user=user, receiver=receiver)

	return redirect("receivers")


@login_required
def remove_receiver(request, pk):
	try:
		to_delete = Receiver.objects.get(pk=pk)
	except:
		return redirect("home")

	if request.user == to_delete.user:
		to_delete.delete()

	return redirect("receivers")


@login_required
def receiver_list(request):
	user = request.user

	context = {
		'receiver_list': Receiver.objects.filter(user=user).order_by('receiver'),
	}

	return render(request, "app/receiver_form.html", context=context)


@login_required
def send_email(request):
	if request.method != 'POST':
		return redirect("home")

	content = request.POST['content']
	subject = request.POST['subject']
	sender = os.environ.get('EMAIL_USER')
	user = request.user

	receivers = [str(receiver) for receiver in Receiver.objects.filter(user=user)]

	if not receivers:
		return redirect("home")

	send_mail(
		subject,
		content,
		sender,
		receivers,
		fail_silently=False,
	)

	return redirect("home")
