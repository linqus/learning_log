from django.shortcuts import render, redirect
from .models import Topic, Entry
from .forms import TopicForm,EntryForm
from django.contrib.auth.decorators import login_required
from django.http import Http404

# Create your views here.

def index(request):
	return render(request,'learning_logs/index.html')

@login_required
def topics(request):
	topics = Topic.objects.filter(owner=request.user).order_by('date_added')
	context = {'topics':topics}
	return render(request,'learning_logs/topics.html',context)

@login_required
def topic(request,**kwargs):
	topic = Topic.objects.get(id=kwargs['id_tematu'])
	if topic.owner != request.user:
		raise Http404
	entries = topic.entry_set.order_by('-date_added')
	context ={'temat': topic, 'wpisy':entries} 
	return render(request,'learning_logs/topic.html',context)

@login_required
def new_topic(request):
	if request.method != 'POST':
		form = TopicForm()
	else:
		form = TopicForm(data=request.POST)
		if form.is_valid():
			new_topic = form.save(commit=False)
			new_topic.owner=request.user
			new_topic.save()
			return redirect('learning_logs_app:tematy')

	context = {'form':form}
	return render(request,'learning_logs/new_topic.html',context)

@login_required
def new_entry(request,id_tematu):
	topic = Topic.objects.get(id=id_tematu)
	if topic.owner != request.user:
		raise Http404
		
	if request.method != 'POST':
		form = EntryForm()
	else:
		form = EntryForm(data=request.POST)
		if form.is_valid():
			new_entry = form.save(commit=False)
			new_entry.topic=topic
			new_entry.save()
			return redirect('learning_logs_app:temat',id_tematu=id_tematu)
	context = {'topic':topic,'form':form}
	return render(request,'learning_logs/new_entry.html',context)

@login_required
def edit_entry(request,id_wpisu):
	entry = Entry.objects.get(id=id_wpisu)
	topic = entry.topic
	if topic.owner != request.user:
		raise Http404
	if request.method != 'POST':
		form = EntryForm(instance=entry)
	else:
		form = EntryForm(instance=entry,data=request.POST)
		if form.is_valid():
			form.save()
			return redirect('learning_logs_app:temat',id_tematu=topic.id)

	context = {'temat':topic,'wpis':entry,'form':form}
	return render(request,'learning_logs/edit_entry.html',context)