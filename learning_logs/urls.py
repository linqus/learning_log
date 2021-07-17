from django.urls import path
from . import views

app_name = 'learning_logs_app'
urlpatterns = [
	path('', views.index, name='index' ),
	path('topics/', views.topics, name='tematy'),
	path('topics/<int:id_tematu>/',views.topic, name='temat'),
	
]