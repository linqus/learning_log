from django.shortcuts import render
from .models import Topic

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