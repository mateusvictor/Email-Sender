from django.urls import path, include
from . import views


urlpatterns = [
	path('', views.home, name="home"),
	path('users/', include('users.urls')),
	path('send_email/', views.send_email, name="send-email"),
	path('receivers/', views.receiver_list, name="receivers"),
	path('receivers/add_receiver/', views.add_receiver, name="add-receiver"),
	path('receivers/remove_receiver/<int:pk>/', views.remove_receiver, name="remove-receiver"),
]