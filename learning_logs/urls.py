from django.urls import path
from . import views

app_name = 'learning_logs_app'
urlpatterns = [
	path('', views.index, name='index' ),
	path('topics/', views.topics, name='tematy'),
	path('topics/<int:id_tematu>/',views.topic, name='temat'),
	path('new_topic/',views.new_topic,name='nowy_temat'),
	path('new_entry/<int:id_tematu>/',views.new_entry,name='nowy_wpis'),
	path('edit_entry/<int:id_wpisu>',views.edit_entry,name='edycja_wpisu')
	
]