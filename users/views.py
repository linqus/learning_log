from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login

# Create your views here.
def register(request):
	
	if request.method != 'POST':
		formularz = UserCreationForm()
	else:
		formularz = UserCreationForm(data=request.POST)
		if formularz.is_valid():
			new_user = formularz.save()
			login(request,new_user)
			return redirect('learning_logs_app:index')
		
	context = {'form':formularz}
	return render(request,'registration/register.html',context)	
