from django.urls import path, include


app_name = 'użytkownik'
urlpatterns = [
	path('', include('django.contrib.auth.urls')),
]