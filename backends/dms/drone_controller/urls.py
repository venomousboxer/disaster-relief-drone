from django.urls import path
from . import views
urlpatterns = [
	path('', views.drone_index, name="index_dc")
]
