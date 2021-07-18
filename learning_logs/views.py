from django.shortcuts import render, redirect
from .models import Topic
from .forms import TopicForm,EntryForm

# Create your views here.

def index(request):
	return render(request,'learning_logs/index.html')

def topics(request):
	topics = Topic.objects.order_by('date_added')
	context = {'topics':topics}
	return render(request,'learning_logs/topics.html',context)


def topic(request,**kwargs):
	topic = Topic.objects.get(id=kwargs['id_tematu'])
	entries = topic.entry_set.order_by('-date_added')
	context ={'temat': topic, 'wpisy':entries} 
	return render(request,'learning_logs/topic.html',context)


def new_topic(request):
	if request.method != 'POST':
		form = TopicForm()
	else:
		form = TopicForm(data=request.POST)
		if form.is_valid():
			form.save()
			return redirect('learning_logs_app:tematy')

	context = {'form':form}
	return render(request,'learning_logs/new_topic.html',context)

def new_entry(request,id_tematu):
	topic = Topic.objects.get(id=id_tematu)

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
